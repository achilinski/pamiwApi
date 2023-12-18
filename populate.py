import random


import os
import django
from faker import Faker
# import your models

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pamiwApi.settings')  # Replace 'your_project.settings' with your actual settings path

django.setup()
fake = Faker()

from api.models import User, Category, Author, Book  # Replace 'myapp' with your app name
def create_categories(n):
    categories = []
    for _ in range(n):
        name = fake.word()
        description = fake.text()
        category = Category(name=name, description=description)
        categories.append(category)
    Category.objects.bulk_create(categories)

def create_authors(n):
    authors = []
    for _ in range(n):
        name = fake.first_name()
        surname = fake.last_name()
        description = fake.text()
        author = Author(name=name, surname=surname, description=description)
        authors.append(author)
    Author.objects.bulk_create(authors)

def create_books(n):
    authors = list(Author.objects.all())
    categories = list(Category.objects.all())
    books = []
    for _ in range(n):
        title = fake.sentence(nb_words=3)
        description = fake.text()
        author = random.choice(authors)
        category = random.choice(categories)
        rating = round(random.uniform(1, 5), 2)
        price = round(random.uniform(5, 50), 2)
        book = Book(title=title, description=description, author=author, category=category, rating=rating, price=price)
        books.append(book)
    Book.objects.bulk_create(books)

def create_users(n):
    users = []
    for _ in range(n):
        name = fake.first_name()
        surname = fake.last_name()
        email = fake.email()
        password = fake.password()
        is_admin = False
        is_active = fake.boolean()
        is_staff = False
        is_superuser = False
        user = User(name=name, surname=surname, email=email, password=password, is_admin=is_admin, is_active=is_active, is_staff=is_staff, is_superuser=is_superuser)
        users.append(user)
    User.objects.bulk_create(users)

def assign_books_to_users():
    users = User.objects.all()
    for user in users:
        books = Book.objects.order_by('?')[:random.randint(1, 5)]  # Assign 1-5 random books to each user
        user.read_books.set(books)

def populate_database():
    create_categories(10)
    create_authors(15)
    create_books(50)
    create_users(20)
    assign_books_to_users()

# Run the population script
populate_database()
