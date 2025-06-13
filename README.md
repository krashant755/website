# ShopEase E-commerce Website

ShopEase is a fully-featured e-commerce website built with Django. It includes user authentication, product catalog, shopping cart, wishlist, and checkout functionality.

## Features

- User authentication (login, signup)
- Product catalog with categories
- Shopping cart functionality
- Wishlist feature
- Checkout process for both guest and logged-in users
- Responsive, modern UI design

## UI Design

The website features a modern, creative UI with:

- Custom color scheme with CSS variables
- Animated elements using AOS (Animate On Scroll)
- Card-based design with hover effects
- Modern typography with Google Fonts (Inter)
- Responsive layout for all screen sizes
- Interactive components (tooltips, dropdowns)
- Creative product and category cards
- Custom hero section with gradient background
- Animated navigation elements
- Consistent design language throughout

## Demo Accounts

- Customer: username `customer`, password `Password123`
- Admin: username `admin`, password `AdminPass123`

## Local Setup Instructions

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. Copy `env.example` to `.env` and set your environment variables
5. Install dependencies: `pip install -r requirements.txt`
6. Run migrations: `python manage.py migrate`
7. Load demo data: `python manage.py loaddata demo_data.json`
8. Run the development server: `python manage.py runserver`
9. Access the website at http://127.0.0.1:8000/

## Deployment on Render

### Prerequisites
- A [Render](https://render.com/) account
- A PostgreSQL database (you can create one on Render)

### Steps

1. Fork or clone this repository to your GitHub account
2. Create a new Web Service on Render
3. Connect your GitHub repository
4. Configure the following settings:
   - **Name**: Your app name
   - **Environment**: Python
   - **Region**: Choose the closest region
   - **Branch**: main (or your preferred branch)
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn ecommerce.wsgi:application`
5. Add the following environment variables:
   - `SECRET_KEY`: Your Django secret key
   - `DEBUG`: False
   - `ALLOWED_HOSTS`: Your Render URL (e.g., your-app.onrender.com)
   - `DATABASE_URL`: Your PostgreSQL connection string
6. Click "Create Web Service"

Render will automatically deploy your application and provide you with a URL to access it.

## Project Structure

- `store/`: Main app for products, categories, and browsing
- `users/`: User authentication and profiles
- `cart/`: Shopping cart and checkout functionality
- `templates/`: HTML templates
- `static/`: Static files (CSS, JavaScript, images)
- `media/`: User-uploaded files

## Technologies Used

- Django 5.2
- Python 3.13
- Bootstrap 5
- HTML5 & CSS3
- JavaScript
- SQLite (development) / PostgreSQL (production)
- Font Awesome icons
- AOS Animation Library
- Whitenoise for static files
- Gunicorn for production server

