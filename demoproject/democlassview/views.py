from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse

class SimpleFormView(TemplateView):
    template_name = "democlassview/form.html"

    def get(self, request, *args, **kwargs):
        # Handle GET request
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        # Handle POST request
        name = request.POST.get('name')
        message = request.POST.get('message')

        # For simplicity, return a response directly
        return HttpResponse(f"Thank you, {name}. Your message: '{message}' was received!")
