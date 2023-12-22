from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300)
    author = models.CharField(max_length=150)
    isbn = models.CharField(max_length=13)
    price = models.DecimalField(max_digits=30, decimal_places=2)
    content = models.TextField(max_length=2000, null=True)

    def __str__(self):
        return self.title