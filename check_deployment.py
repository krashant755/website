#!/usr/bin/env python
"""
Deployment check script for the ecommerce project.
Run this script before deploying to check for common issues.
"""

import os
import sys
import importlib.util
import subprocess
import re

def check_python_version():
    """Check if Python version is compatible."""
    print("\n🔍 Checking Python version...")
    
    version = sys.version_info
    if version.major == 3 and version.minor >= 8:
        print("✅ Python version is compatible:", sys.version)
        return True
    else:
        print("❌ Python version is not compatible:", sys.version)
        print("   Recommended: Python 3.8 or higher")
        return False

def check_required_files():
    """Check if required files exist."""
    print("\n🔍 Checking required files...")
    
    required_files = [
        "requirements.txt",
        "Procfile",
        "build.sh",
        "runtime.txt",
        "render.yaml",
        "ecommerce/production.py",
        "ecommerce/wsgi.py",
        "ecommerce/settings.py",
    ]
    
    all_exist = True
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path} exists")
        else:
            print(f"❌ {file_path} does not exist")
            all_exist = False
    
    return all_exist

def check_dependencies():
    """Check if all required dependencies are in requirements.txt."""
    print("\n🔍 Checking dependencies...")
    
    required_deps = [
        "django",
        "gunicorn",
        "whitenoise",
        "dj-database-url",
        "psycopg2-binary",
    ]
    
    try:
        with open("requirements.txt", "r") as f:
            content = f.read().lower()
        
        all_deps_found = True
        for dep in required_deps:
            if dep.lower() in content:
                print(f"✅ {dep} found in requirements.txt")
            else:
                print(f"❌ {dep} not found in requirements.txt")
                all_deps_found = False
        
        return all_deps_found
    except FileNotFoundError:
        print("❌ requirements.txt not found")
        return False

def check_procfile():
    """Check if Procfile has the correct configuration."""
    print("\n🔍 Checking Procfile configuration...")
    
    try:
        with open("Procfile", "r") as f:
            content = f.read().strip()
        
        if re.match(r"web:\s*gunicorn\s+ecommerce\.wsgi:application", content):
            print("✅ Procfile configuration looks good")
            return True
        else:
            print("❌ Procfile configuration might be incorrect")
            print(f"   Current: {content}")
            print("   Expected: web: gunicorn ecommerce.wsgi:application")
            return False
    except FileNotFoundError:
        print("❌ Procfile not found")
        return False

def check_static_files():
    """Check static files configuration."""
    print("\n🔍 Checking static files configuration...")
    
    # Check if staticfiles directory exists
    if os.path.exists("staticfiles"):
        print("✅ staticfiles directory exists")
    else:
        print("❌ staticfiles directory does not exist")
        print("   Run: mkdir -p staticfiles")
    
    # Check if static/css directory exists
    if os.path.exists("static/css"):
        print("✅ static/css directory exists")
    else:
        print("❌ static/css directory does not exist")
        print("   Run: mkdir -p static/css")
    
    # Check if style.css exists
    if os.path.exists("static/css/style.css"):
        print("✅ static/css/style.css exists")
    else:
        print("❌ static/css/style.css does not exist")
        print("   Create a CSS file at static/css/style.css")
    
    # Check whitenoise in settings
    try:
        with open("ecommerce/settings.py", "r") as f:
            settings_content = f.read()
        
        if "whitenoise.middleware.WhiteNoiseMiddleware" in settings_content:
            print("✅ WhiteNoise middleware is configured in settings.py")
        else:
            print("❌ WhiteNoise middleware not found in settings.py")
            print("   Add 'whitenoise.middleware.WhiteNoiseMiddleware' to MIDDLEWARE")
        
        if "STATICFILES_STORAGE" in settings_content and "whitenoise" in settings_content:
            print("✅ STATICFILES_STORAGE is configured for WhiteNoise")
        else:
            print("❌ STATICFILES_STORAGE might not be configured for WhiteNoise")
    except FileNotFoundError:
        print("❌ ecommerce/settings.py not found")
    
    return True

def check_build_script():
    """Check if build.sh has the correct configuration."""
    print("\n🔍 Checking build.sh script...")
    
    try:
        with open("build.sh", "r") as f:
            content = f.read()
        
        checks = {
            "pip install": "pip install" in content,
            "collectstatic": "collectstatic" in content,
            "migrate": "migrate" in content,
        }
        
        all_checks_passed = all(checks.values())
        
        for check, passed in checks.items():
            if passed:
                print(f"✅ {check} command found in build.sh")
            else:
                print(f"❌ {check} command not found in build.sh")
        
        # Check if the script is executable
        if os.access("build.sh", os.X_OK):
            print("✅ build.sh is executable")
        else:
            print("❌ build.sh is not executable")
            print("   Run: chmod +x build.sh")
            all_checks_passed = False
        
        return all_checks_passed
    except FileNotFoundError:
        print("❌ build.sh not found")
        return False

def main():
    """Run all checks and provide a summary."""
    print("=" * 60)
    print("📋 DEPLOYMENT CHECK FOR ECOMMERCE PROJECT")
    print("=" * 60)
    
    checks = [
        ("Python version", check_python_version()),
        ("Required files", check_required_files()),
        ("Dependencies", check_dependencies()),
        ("Procfile", check_procfile()),
        ("Static files", check_static_files()),
        ("Build script", check_build_script()),
    ]
    
    print("\n" + "=" * 60)
    print("📋 SUMMARY")
    print("=" * 60)
    
    all_passed = True
    for name, result in checks:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {name}")
        if not result:
            all_passed = False
    
    print("\n" + "=" * 60)
    if all_passed:
        print("🎉 All checks passed! Your project is ready for deployment.")
    else:
        print("⚠️  Some checks failed. Please fix the issues before deploying.")
    print("=" * 60)
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main()) 