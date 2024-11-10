from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as necessary

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # Add other fields as necessary

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as necessary