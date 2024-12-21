from django.shortcuts import render
from rest_framework import renderers, generics
from .models import Category_F_O, MenuItem_F_O
from .serializers import CategoryFOSerializer, MenuItemFOSerializer

# Create your views here.
class CategoriesFOView(generics.ListCreateAPIView):
    queryset = Category_F_O.objects.all()
    serializer_class = CategoryFOSerializer

class MenuItemFOView(generics.ListCreateAPIView):
    queryset = MenuItem_F_O.objects.all()
    serializer_class = MenuItemFOSerializer

    ordering_fields = ['price', 'inventory']
    filterset_fileds = ['pirce', 'inventory']
    search_fields = ['category']
