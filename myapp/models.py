from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_date = models.DateTimeField()
    price = models.DecimalField(max_digits=6, decimal_places=2)