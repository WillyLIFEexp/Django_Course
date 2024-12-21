from django.db import models

# Create your models here.
class Category_F_O(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=225)

    def __str__(self)-> str:
        return self.title

class MenuItem_F_O(models.Model):
    title = models.CharField(max_length=225)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.SmallIntegerField()
    category = models.ForeignKey(Category_F_O, on_delete=models.PROTECT, default=1)

    def __str__(self)-> str:
        return self.title

