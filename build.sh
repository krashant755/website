#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Creating staticfiles directory if it doesn't exist..."
mkdir -p staticfiles/css

echo "Explicitly copying CSS files..."
cp -r static/css/* staticfiles/css/

echo "Collecting static files..."
python manage.py collectstatic --no-input

echo "Running migrations..."
python manage.py migrate

echo "Build completed successfully!" 