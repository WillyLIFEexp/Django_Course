from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

    # The above method is the same as the below
    # name = forms.CharField(max_length=100)  # Corresponds to models.CharField(max_length=100)
    # email = forms.EmailField()             # Corresponds to models.EmailField()
    # message = forms.CharField(widget=forms.Textarea)  # Corresponds to models.TextField()
