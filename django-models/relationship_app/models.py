from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as necessary

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publishers = models.ManyToManyField(Publisher)
    # Add other fields as necessary

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as necessary
