from django.urls import path
from . import views

urlpatterns = [
    path('', views.books),
    path('basic_drf', views.BookView.as_view()),
    path('basic_drf/<int:pk>', views.SingleBookView.as_view())
]
