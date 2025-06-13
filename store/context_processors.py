from .models import Category

def categories_context(request):
    """
    Context processor to make categories available to all templates.
    """
    try:
        categories = Category.objects.all()
    except Exception:
        # Return an empty list if there's any error
        categories = []
    
    return {'categories': categories} 