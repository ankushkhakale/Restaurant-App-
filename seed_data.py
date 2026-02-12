import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_project.settings')
django.setup()

from menu.models import Category, MenuItem

def seed():
    # Clear existing data
    MenuItem.objects.all().delete()
    Category.objects.all().delete()

    # Create Categories
    starters = Category.objects.create(name='Starters', description='Appetizers to start your meal.')
    main_course = Category.objects.create(name='Main Course', description='Hearty dishes to satisfy your hunger.')
    drinks = Category.objects.create(name='Drinks', description='Refreshing beverages.')

    # Create Menu Items
    MenuItem.objects.create(
        category=starters,
        name='Spring Rolls',
        description='Crispy vegetable spring rolls served with sweet chili sauce.',
        price=5.99
    )
    MenuItem.objects.create(
        category=starters,
        name='Garlic Bread',
        description='Toasted baguette with garlic butter and herbs.',
        price=4.50
    )

    MenuItem.objects.create(
        category=main_course,
        name='Grilled Salmon',
        description='Fresh salmon fillet grilled to perfection, served with asparagus.',
        price=18.99
    )
    MenuItem.objects.create(
        category=main_course,
        name='Pasta Carbonara',
        description='Spaghetti with creamy egg sauce, pancetta, and parmesan.',
        price=14.50
    )

    MenuItem.objects.create(
        category=drinks,
        name='Fresh Lime Soda',
        description='Sparkling soda with fresh lime juice and mint.',
        price=3.99
    )
    
    print("Database seeded successfully!")

if __name__ == '__main__':
    seed()
