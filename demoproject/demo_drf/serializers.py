from rest_framework import serializers
from .models import Book_DRF

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book_DRF
        fields = ['id', 'title', 'author', 'price']