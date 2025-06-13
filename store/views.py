from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from .models import Product, Category
import datetime
import os

def home(request):
    featured_products = Product.objects.filter(is_featured=True)[:8]
    latest_products = Product.objects.order_by('-created_at')[:8]
    
    context = {
        'featured_products': featured_products,
        'latest_products': latest_products,
    }
    return render(request, 'store/home.html', context)

def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    
    category_id = request.GET.get('category')
    if category_id:
        products = products.filter(category__id=category_id)
    
    context = {
        'products': products,
        'categories': categories,
        'selected_category': int(category_id) if category_id else None,
    }
    return render(request, 'store/product_list.html', context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    related_products = Product.objects.filter(category=product.category).exclude(id=product_id)[:4]
    
    context = {
        'product': product,
        'related_products': related_products,
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

def health_check(request):
    """
    A simple health check endpoint to verify the application is running.
    """
    return HttpResponse("OK", content_type="text/plain")

def maintenance(request):
    """
    A maintenance page that shows debug information.
    """
    context = {
        'STATIC_ROOT': os.environ.get('STATIC_ROOT', 'Not set'),
        'STATIC_URL': os.environ.get('STATIC_URL', '/static/'),
        'DEBUG': os.environ.get('DEBUG', 'False'),
        'now': datetime.datetime.now(),
    }
    return render(request, 'maintenance.html', context)

def debug_static(request):
    """
    Debug endpoint to check static file configuration.
    """
    static_root = os.environ.get('STATIC_ROOT', 'Not set')
    static_url = os.environ.get('STATIC_URL', '/static/')
    
    # Check if staticfiles directory exists
    staticfiles_exists = os.path.exists('staticfiles')
    css_dir_exists = os.path.exists('staticfiles/css')
    style_css_exists = os.path.exists('staticfiles/css/style.css')
    
    # Check if static directory exists
    static_exists = os.path.exists('static')
    static_css_exists = os.path.exists('static/css')
    static_style_exists = os.path.exists('static/css/style.css')
    
    data = {
        'static_root': static_root,
        'static_url': static_url,
        'staticfiles_exists': staticfiles_exists,
        'css_dir_exists': css_dir_exists,
        'style_css_exists': style_css_exists,
        'static_exists': static_exists,
        'static_css_exists': static_css_exists,
        'static_style_exists': static_style_exists,
    }
    
    return JsonResponse(data)
