from django.urls import path
from .views import ContactFormView
from django.views.generic import TemplateView

urlpatterns = [
    path('contact/', ContactFormView.as_view(), name='contact_form'),
    path('thank-you/', TemplateView.as_view(template_name='thank_you.html'), name='thank_you'),
]
