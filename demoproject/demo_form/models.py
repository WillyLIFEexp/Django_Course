from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

class Items(models.Model):
    name = models.CharField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    message = models.TextField(null=True)