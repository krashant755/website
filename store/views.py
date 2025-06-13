from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Product, Category

def home(request):
    products = Product.objects.filter(available=True)[:8]  # Get latest 8 products
    categories = Category.objects.all()[:6]  # Get first 6 categories
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'store/home.html', context)

def product_list(request):
    category_slug = request.GET.get('category')
    search_query = request.GET.get('q')
    
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) | 
            Q(description__icontains=search_query)
        )
    
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'store/product_list.html', context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
    
    wishlist_status = False
    if request.user.is_authenticated:
        wishlist_status = product.wishlist_set.filter(user=request.user).exists()
    
    context = {
        'product': product,
        'related_products': related_products,
        'wishlist_status': wishlist_status,
    }
    return render(request, 'store/product_detail.html', context)

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category, available=True)
    
    context = {
        'category': category,
        'products': products,
    }
    return render(request, 'store/category_detail.html', context)
