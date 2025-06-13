from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from store.models import Product
from .models import Cart, CartItem, Order, OrderItem
from .forms import OrderForm

def _get_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, defaults={'cart_id': request.session.session_key})
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        cart, created = Cart.objects.get_or_create(cart_id=session_key)
    
    return cart

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = _get_cart(request)
    
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        if cart_item.quantity < product.stock:
            cart_item.quantity += 1
            cart_item.save()
    except CartItem.DoesNotExist:
        CartItem.objects.create(product=product, cart=cart, quantity=1)
    
    messages.success(request, f'Added {product.name} to your cart')
    return redirect('cart')

def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    if request.user.is_authenticated:
        if cart_item.cart.user == request.user or cart_item.cart.cart_id == request.session.session_key:
            cart_item.delete()
    else:
        if cart_item.cart.cart_id == request.session.session_key:
            cart_item.delete()
    
    messages.success(request, f'Removed {cart_item.product.name} from your cart')
    return redirect('cart')

def update_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    quantity = int(request.POST.get('quantity'))
    
    if quantity > 0 and quantity <= cart_item.product.stock:
        cart_item.quantity = quantity
        cart_item.save()
    elif quantity > cart_item.product.stock:
        messages.warning(request, f'Only {cart_item.product.stock} {cart_item.product.name} available')
        cart_item.quantity = cart_item.product.stock
        cart_item.save()
    
    return redirect('cart')

def cart_view(request):
    try:
        cart = _get_cart(request)
        cart_items = CartItem.objects.filter(cart=cart)
    except Exception as e:
        cart_items = []
    
    context = {
        'cart_items': cart_items,
    }
    return render(request, 'cart/cart.html', context)

def checkout(request):
    cart = _get_cart(request)
    cart_items = CartItem.objects.filter(cart=cart, is_active=True)
    
    if cart_items.count() <= 0:
        return redirect('product_list')
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if request.user.is_authenticated:
                order.user = request.user
            
            order.order_total = sum(item.sub_total() for item in cart_items)
            order.ip = request.META.get('REMOTE_ADDR')
            order.save()
            
            # Create order items
            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price
                )
                
                # Reduce stock
                product = item.product
                product.stock -= item.quantity
                product.save()
            
            # Clear the cart
            cart_items.delete()
            
            return render(request, 'cart/order_complete.html', {'order': order})
    else:
        initial_data = {}
        if request.user.is_authenticated:
            try:
                profile = request.user.profile
                initial_data = {
                    'first_name': request.user.first_name,
                    'last_name': request.user.last_name,
                    'email': request.user.email,
                    'phone': profile.phone,
                    'address': profile.address,
                    'city': profile.city,
                    'state': profile.state,
                    'zip_code': profile.zip_code,
                    'country': profile.country,
                }
            except:
                pass
        form = OrderForm(initial=initial_data)
    
    context = {
        'form': form,
        'cart_items': cart_items,
        'total': sum(item.sub_total() for item in cart_items),
    }
    return render(request, 'cart/checkout.html', context)

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    context = {
        'orders': orders
    }
    return render(request, 'cart/order_history.html', context)

def order_detail(request, order_id):
    if request.user.is_authenticated:
        order = get_object_or_404(Order, order_number=order_id, user=request.user)
    else:
        order = get_object_or_404(Order, order_number=order_id)
    
    order_items = OrderItem.objects.filter(order=order)
    context = {
        'order': order,
        'order_items': order_items
    }
    return render(request, 'cart/order_detail.html', context)
