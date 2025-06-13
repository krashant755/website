#!/usr/bin/env python
"""
A script to check if static files are properly configured.
"""

import os
import sys
import django
from django.conf import settings
from django.contrib.staticfiles.finders import find
from django.contrib.staticfiles.storage import staticfiles_storage

def check_static_files():
    """Check if static files are properly configured."""
    print("Checking static files configuration...")
    
    # Check STATIC_URL
    print(f"STATIC_URL: {settings.STATIC_URL}")
    
    # Check STATIC_ROOT
    print(f"STATIC_ROOT: {settings.STATIC_ROOT}")
    
    # Check STATICFILES_DIRS
    print(f"STATICFILES_DIRS: {settings.STATICFILES_DIRS}")
    
    # Check STATICFILES_STORAGE
    print(f"STATICFILES_STORAGE: {settings.STATICFILES_STORAGE}")
    
    # Check if style.css exists
    style_css_path = find('css/style.css')
    if style_css_path:
        print(f"✅ css/style.css found at: {style_css_path}")
    else:
        print("❌ css/style.css not found")
    
    # Check if test.css exists
    test_css_path = find('css/test.css')
    if test_css_path:
        print(f"✅ css/test.css found at: {test_css_path}")
    else:
        print("❌ css/test.css not found")
    
    # Check if staticfiles directory exists
    if os.path.exists(settings.STATIC_ROOT):
        print(f"✅ staticfiles directory exists at: {settings.STATIC_ROOT}")
        # List files in staticfiles directory
        files = os.listdir(settings.STATIC_ROOT)
        print(f"Files in staticfiles directory: {len(files)} files")
        if 'css' in files:
            css_files = os.listdir(os.path.join(settings.STATIC_ROOT, 'css'))
            print(f"CSS files in staticfiles directory: {css_files}")
    else:
        print("❌ staticfiles directory doesn't exist")

def main():
    """Main function"""
    print("Django Static Files Check")
    print("========================")
    
    # Set up Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
    django.setup()
    
    # Run checks
    check_static_files()
    
    print("\nCheck completed!")

if __name__ == "__main__":
    main() 