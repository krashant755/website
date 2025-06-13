#!/usr/bin/env python
"""
A script to check for common deployment issues.
Run this before deploying to Render.
"""

import os
import sys
import importlib
import django
from django.conf import settings

def check_context_processors():
    """Check that context processors exist"""
    print("Checking context processors...")
    
    # Check store context processor
    try:
        from store import context_processors
        if hasattr(context_processors, 'categories_context'):
            print("✅ store.context_processors.categories_context exists")
        else:
            print("❌ store.context_processors.categories_context is missing")
    except ImportError:
        print("❌ store.context_processors module is missing")
    
    # Check cart context processor
    try:
        from cart import context_processors
        if hasattr(context_processors, 'cart_context'):
            print("✅ cart.context_processors.cart_context exists")
        else:
            print("❌ cart.context_processors.cart_context is missing")
    except ImportError:
        print("❌ cart.context_processors module is missing")

def check_settings():
    """Check settings configuration"""
    print("\nChecking settings...")
    
    # Check if production.py exists
    if os.path.exists('ecommerce/production.py'):
        print("✅ ecommerce/production.py exists")
    else:
        print("❌ ecommerce/production.py is missing")
    
    # Check context processors in settings
    context_processors = settings.TEMPLATES[0]['OPTIONS']['context_processors']
    if 'store.context_processors.categories_context' in context_processors:
        print("✅ store.context_processors.categories_context in settings")
    else:
        print("❌ store.context_processors.categories_context not in settings")
    
    if 'cart.context_processors.cart_context' in context_processors:
        print("✅ cart.context_processors.cart_context in settings")
    else:
        print("❌ cart.context_processors.cart_context not in settings")

def check_static_files():
    """Check static files configuration"""
    print("\nChecking static files...")
    
    # Check if staticfiles directory exists
    if os.path.exists('staticfiles'):
        print("✅ staticfiles directory exists")
    else:
        print("❌ staticfiles directory is missing")
    
    # Check if STATIC_ROOT is set
    if hasattr(settings, 'STATIC_ROOT') and settings.STATIC_ROOT:
        print(f"✅ STATIC_ROOT is set to {settings.STATIC_ROOT}")
    else:
        print("❌ STATIC_ROOT is not set")
    
    # Check if whitenoise is installed
    try:
        import whitenoise
        print("✅ whitenoise is installed")
    except ImportError:
        print("❌ whitenoise is not installed")

def main():
    """Main function"""
    print("Django Deployment Check")
    print("======================")
    
    # Set up Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
    django.setup()
    
    # Run checks
    check_context_processors()
    check_settings()
    check_static_files()
    
    print("\nCheck completed!")

if __name__ == "__main__":
    main() 