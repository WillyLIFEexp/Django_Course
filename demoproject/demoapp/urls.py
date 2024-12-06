from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('next', views.next_url, name="next_url"),
]