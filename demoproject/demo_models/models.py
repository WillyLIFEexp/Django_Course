from django.db import models

# Create your models here.
class Items(models.Model):
    id = models.IntegerField(primary_key=True) # Field for storing Int data
    name = models.CharField(max_length=300) # Field for storing Str data
    price = models.FloatField() # Field for storing Float data
    stock = models.BooleanField(default=True) # Field for storing Bool data
    created_date = models.DateField(auto_now_add=True) # Field for storing Date data
    created_time = models.DateTimeField(auto_now_add=True) # Field for storing Datetime data
    additional_data = models.JSONField(default=dict)  # Field for storing JSON data

# Practie for ForeignKey
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    '''
    Choose on_delete Based on Business Logic:
        - Use CASCADE for dependent objects that should be deleted together.
        - Use PROTECT if deletion should be prevented when there are related objects.
        - Use SET_NULL if the referenced object is deleted, then assigns a specific value or calls a callable function
        - Use SET_DEFAULT for preserve the related objects but remove their association with the deleted object.
        - Use Set() for assigns a specific value or calls a callable function to set the ForeignKey field when the referenced object is deleted.
    '''
    def custom_value():
        return 42

    author = models.ForeignKey('Author', on_delete=models.SET(custom_value))
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)

    # Set
    # author = models.ForeignKey('Author', on_delete=models.SET(custom_value))

    # SET_NULL
    # author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)

    # SET_DEFAULT
    # author = models.ForeignKey(Author, on_delete=models.SET_DEFAULT, default=1)
