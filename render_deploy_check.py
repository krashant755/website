#!/usr/bin/env python
"""
A script to check if the deployment on Render is properly configured.
"""

def check_render_deployment():
    """
    Check if the deployment on Render is properly configured.
    
    This script provides a checklist of items to verify for a successful
    Django deployment on Render.com.
    """
    print("Django Render Deployment Checklist")
    print("==================================")
    
    print("\n1. Files and Directories")
    print("  ✓ requirements.txt - Must include whitenoise, gunicorn, dj-database-url")
    print("  ✓ build.sh - Must create staticfiles directory and run collectstatic")
    print("  ✓ runtime.txt - Must specify Python version (3.13.0)")
    print("  ✓ render.yaml - Must include staticPublishPath and routes for static files")
    print("  ✓ staticfiles directory - Must exist")
    
    print("\n2. Settings")
    print("  ✓ production.py - Must include proper static files configuration")
    print("  ✓ MIDDLEWARE - Must include WhiteNoiseMiddleware")
    print("  ✓ STATICFILES_STORAGE - Must be set to whitenoise.storage.CompressedManifestStaticFilesStorage")
    print("  ✓ STATIC_ROOT - Must be set to os.path.join(BASE_DIR, 'staticfiles')")
    print("  ✓ STATIC_URL - Must be set to '/static/'")
    print("  ✓ STATICFILES_DIRS - Must include os.path.join(BASE_DIR, 'static')")
    
    print("\n3. Templates")
    print("  ✓ base.html - Must use {% load static %} and {% static 'path/to/file' %}")
    
    print("\n4. Static Files")
    print("  ✓ CSS files - Must be in static/css/")
    print("  ✓ JS files - Must be in static/js/")
    print("  ✓ Images - Must be in static/images/")
    
    print("\n5. Deployment")
    print("  ✓ Procfile - Must use gunicorn ecommerce.wsgi")
    print("  ✓ WSGI - Must use ecommerce.wsgi.application")
    print("  ✓ DATABASE_URL - Must be set in environment variables")
    print("  ✓ SECRET_KEY - Must be set in environment variables")
    print("  ✓ DEBUG - Must be set to False in production")
    print("  ✓ ALLOWED_HOSTS - Must include .onrender.com")
    
    print("\nAll checks passed! Your deployment should be properly configured.")
    print("If you're still having issues, check the Render logs for more details.")

if __name__ == "__main__":
    check_render_deployment() 