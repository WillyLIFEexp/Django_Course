from django.urls import path
from . import views

urlpatterns = [
    path('category', views.CategoriesFOView.as_view()),
    path('menu-items', views.MenuItemFOView.as_view()),
]
