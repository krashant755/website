import os
import django
import random
from datetime import datetime, timedelta
from pathlib import Path

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

# Import Django modules after setup
from django.utils import timezone
from django.core.files import File
from django.contrib.auth.models import User
from store.models import Category, Product
from users.models import Profile, Wishlist
from cart.models import Order, OrderItem

def create_users():
    # Create regular user
    try:
        user = User.objects.create_user(
            username='customer',
            email='customer@example.com',
            password='Password123',
            first_name='John',
            last_name='Doe'
        )
        profile = Profile.objects.create(
            user=user,
            address='123 Main St',
            city='Anytown',
            state='CA',
            zip_code='12345',
            country='USA',
            phone='555-123-4567'
        )
        print("Created user: customer")
    except:
        print("User 'customer' already exists")
    
    # Create superuser
    try:
        admin = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='AdminPass123'
        )
        print("Created admin user: admin")
    except:
        print("User 'admin' already exists")

def create_categories():
    categories_data = [
        {
            'name': 'Electronics',
            'slug': 'electronics',
            'description': 'Discover the latest electronics gadgets and technology.'
        },
        {
            'name': 'Clothing',
            'slug': 'clothing',
            'description': 'Shop fashionable clothing for all occasions.'
        },
        {
            'name': 'Books',
            'slug': 'books',
            'description': 'Explore a wide range of books across various genres.'
        },
        {
            'name': 'Home & Kitchen',
            'slug': 'home-kitchen',
            'description': 'Find everything you need for your home and kitchen.'
        },
        {
            'name': 'Sports & Outdoors',
            'slug': 'sports-outdoors',
            'description': 'Gear up for your favorite sports and outdoor activities.'
        }
    ]
    
    for cat_data in categories_data:
        try:
            category = Category.objects.create(
                name=cat_data['name'],
                slug=cat_data['slug'],
                description=cat_data['description']
            )
            print(f"Created category: {category.name}")
        except:
            print(f"Category '{cat_data['name']}' already exists")

def create_products():
    # Make sure we have categories
    if Category.objects.count() == 0:
        print("No categories found. Creating categories first.")
        create_categories()
    
    electronics = Category.objects.get(slug='electronics')
    clothing = Category.objects.get(slug='clothing')
    books = Category.objects.get(slug='books')
    home_kitchen = Category.objects.get(slug='home-kitchen')
    sports = Category.objects.get(slug='sports-outdoors')
    
    products_data = [
        {
            'name': 'Smartphone X',
            'slug': 'smartphone-x',
            'description': 'Latest smartphone with cutting-edge features. High-resolution display, powerful processor, and all-day battery life.',
            'price': 799.99,
            'stock': 25,
            'category': electronics
        },
        {
            'name': 'Laptop Pro',
            'slug': 'laptop-pro',
            'description': 'Professional-grade laptop for demanding tasks. Features a high-performance processor, dedicated graphics, and fast SSD storage.',
            'price': 1299.99,
            'stock': 15,
            'category': electronics
        },
        {
            'name': 'Wireless Earbuds',
            'slug': 'wireless-earbuds',
            'description': 'True wireless earbuds with noise cancellation and premium sound quality. Long battery life and comfortable fit.',
            'price': 149.99,
            'stock': 40,
            'category': electronics
        },
        {
            'name': 'Smart Watch',
            'slug': 'smart-watch',
            'description': 'Track your fitness, sleep, and more with this advanced smartwatch. Water-resistant and compatible with iOS and Android.',
            'price': 249.99,
            'stock': 30,
            'category': electronics
        },
        {
            'name': 'Men\'s Casual T-Shirt',
            'slug': 'mens-casual-tshirt',
            'description': 'Comfortable cotton t-shirt for everyday wear. Available in multiple colors and sizes.',
            'price': 19.99,
            'stock': 50,
            'category': clothing
        },
        {
            'name': 'Women\'s Summer Dress',
            'slug': 'womens-summer-dress',
            'description': 'Lightweight and stylish summer dress perfect for warm weather. Flattering cut and breathable fabric.',
            'price': 39.99,
            'stock': 35,
            'category': clothing
        },
        {
            'name': 'Running Shoes',
            'slug': 'running-shoes',
            'description': 'High-performance running shoes with excellent cushioning and support. Breathable and lightweight design for comfort during long runs.',
            'price': 89.99,
            'stock': 25,
            'category': clothing
        },
        {
            'name': 'Best-Selling Novel',
            'slug': 'bestselling-novel',
            'description': 'Award-winning novel that has captivated readers worldwide. A compelling story of adventure, love, and self-discovery.',
            'price': 14.99,
            'stock': 60,
            'category': books
        },
        {
            'name': 'Cookbook Collection',
            'slug': 'cookbook-collection',
            'description': 'Collection of international recipes from a renowned chef. Includes detailed instructions and beautiful food photography.',
            'price': 24.99,
            'stock': 20,
            'category': books
        },
        {
            'name': 'Coffee Maker',
            'slug': 'coffee-maker',
            'description': 'Programmable coffee maker with multiple brewing options. Makes up to 12 cups and has a built-in grinder for the freshest coffee.',
            'price': 79.99,
            'stock': 18,
            'category': home_kitchen
        },
        {
            'name': 'Non-Stick Cookware Set',
            'slug': 'cookware-set',
            'description': 'Complete set of non-stick pots and pans for all your cooking needs. Durable, easy to clean, and dishwasher safe.',
            'price': 129.99,
            'stock': 15,
            'category': home_kitchen
        },
        {
            'name': 'Yoga Mat',
            'slug': 'yoga-mat',
            'description': 'Premium yoga mat with excellent grip and cushioning. Non-slip surface and easy to clean. Perfect for yoga, pilates, and other floor exercises.',
            'price': 29.99,
            'stock': 45,
            'category': sports
        },
        {
            'name': 'Hiking Backpack',
            'slug': 'hiking-backpack',
            'description': 'Durable and comfortable hiking backpack with multiple compartments. Water-resistant and includes a hydration system compatibility.',
            'price': 59.99,
            'stock': 22,
            'category': sports
        }
    ]
    
    for prod_data in products_data:
        try:
            product = Product.objects.create(
                name=prod_data['name'],
                slug=prod_data['slug'],
                description=prod_data['description'],
                price=prod_data['price'],
                stock=prod_data['stock'],
                category=prod_data['category']
            )
            print(f"Created product: {product.name}")
        except Exception as e:
            print(f"Product '{prod_data['name']}' already exists or error: {e}")

def create_wishlists():
    try:
        user = User.objects.get(username='customer')
        # Add some random products to the wishlist
        products = list(Product.objects.all())[:4]  # First 4 products
        
        for product in products:
            wishlist, created = Wishlist.objects.get_or_create(
                user=user,
                product=product
            )
            if created:
                print(f"Added {product.name} to {user.username}'s wishlist")
            else:
                print(f"{product.name} already in {user.username}'s wishlist")
    except User.DoesNotExist:
        print("User 'customer' not found")

def create_orders():
    try:
        user = User.objects.get(username='customer')
        profile = user.profile
        
        # Create a past order
        past_date = timezone.now() - timedelta(days=10)
        
        order = Order.objects.create(
            user=user,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            phone=profile.phone,
            address=profile.address,
            city=profile.city,
            state=profile.state,
            zip_code=profile.zip_code,
            country=profile.country,
            order_total=0,
            status='Delivered',
            is_ordered=True
        )
        
        # Add some random products to the order
        products = list(Product.objects.all())[:3]  # First 3 products
        total = 0
        
        for product in products:
            quantity = random.randint(1, 3)
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price=product.price
            )
            total += product.price * quantity
        
        order.order_total = total
        order.created_at = past_date
        order.updated_at = past_date + timedelta(days=2)
        order.save()
        
        print(f"Created past order: {order.order_number}")
        
        # Create a recent order
        recent_date = timezone.now() - timedelta(days=2)
        
        order = Order.objects.create(
            user=user,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            phone=profile.phone,
            address=profile.address,
            city=profile.city,
            state=profile.state,
            zip_code=profile.zip_code,
            country=profile.country,
            order_total=0,
            status='Processing',
            is_ordered=True
        )
        
        # Add some random products to the order
        products = list(Product.objects.all())[3:6]  # Next 3 products
        total = 0
        
        for product in products:
            quantity = random.randint(1, 2)
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price=product.price
            )
            total += product.price * quantity
        
        order.order_total = total
        order.created_at = recent_date
        order.save()
        
        print(f"Created recent order: {order.order_number}")
        
    except User.DoesNotExist:
        print("User 'customer' not found")

if __name__ == "__main__":
    print("Creating demo data...")
    create_users()
    create_categories()
    create_products()
    create_wishlists()
    create_orders()
    print("Demo data creation complete!") 