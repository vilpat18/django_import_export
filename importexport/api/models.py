from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    release_data = models.DateField()


class Author(models.Model):
    name = models.CharField(max_length=50)
    biogarphy = models.TextField()
    date_of_birth = models.DateField()
    books = models.ManyToManyField(Book,related_name='author',blank=True)