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
