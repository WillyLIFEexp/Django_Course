from django.urls import path
from .views import SimpleFormView

urlpatterns = [
    path('form/', SimpleFormView.as_view(), name='simple_form'),
]
