from .models import CartItem, Cart

def cart_context(request):
    """
    Context processor to make cart information available to all templates.
    """
    cart_count = 0
    
    try:
        if request.user.is_authenticated:
            # For authenticated users
            cart = Cart.objects.filter(user=request.user).first()
            if cart:
                cart_items = CartItem.objects.filter(cart=cart, is_active=True)
                cart_count = sum(item.quantity for item in cart_items)
        else:
            # For guest users
            session_key = request.session.session_key
            if not session_key:
                request.session.create()
                session_key = request.session.session_key
                
            cart = Cart.objects.filter(cart_id=session_key).first()
            if cart:
                cart_items = CartItem.objects.filter(cart=cart, is_active=True)
                cart_count = sum(item.quantity for item in cart_items)
    except Exception:
        # Fallback in case of any errors
        cart_count = 0
    
    return {'cart_count': cart_count} 