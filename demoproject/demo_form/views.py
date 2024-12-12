from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render
from .forms import ContactForm

class ContactFormView(View):
    template_name = 'contact_form.html'
    success_url = reverse_lazy('thank_you')

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return HttpResponseRedirect(self.success_url)
        return render(request, self.template_name, {'form': form})  # Redisplay the form with errors
