from .models import Cart, CartItem

def cart_context(request):
    try:
        if request.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=request.user, defaults={'cart_id': request.session.session_key})
        else:
            session_key = request.session.session_key
            if not session_key:
                request.session.create()
                session_key = request.session.session_key
            cart, created = Cart.objects.get_or_create(cart_id=session_key)
        
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        cart_count = sum(item.quantity for item in cart_items)
        cart_total = sum(item.sub_total() for item in cart_items)
    except:
        cart_count = 0
        cart_total = 0
        cart_items = []
    
    return {
        'cart_count': cart_count,
        'cart_total': cart_total,
        'cart_items': cart_items,
    } 