from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    read_books = models.ManyToManyField('Book', related_name='read_books')
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

class Author(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    average_rating = models.FloatField(default=0.0)
    description = models.TextField()



class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    rating = models.FloatField()
    price = models.FloatField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.author.average_rating = self.author.book_set.aggregate(models.Avg('rating'))['rating__avg']
        self.author.save()

