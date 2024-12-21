from rest_framework import serializers
from .models import MenuItem_F_O, Category_F_O

class CategoryFOSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category_F_O
        fields = ['id', 'title']

class MenuItemFOSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)
    category = CategoryFOSerializer(read_only=True)

    class Meta:
        model = MenuItem_F_O
        fields = ['id', 'title', 'price', 'inventory', 'category', 'category_id']

    