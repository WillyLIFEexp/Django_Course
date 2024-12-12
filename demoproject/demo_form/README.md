# Forms pratice
## :closed_book: Project Directory Structure
```bash
Django_Course/
├── demo_form/            # App folder
│ │ ├── migrations/       # Migrations detail folder
│ │ │ ├── __init__.py     # Migrate init file
│ │ │ ├── 0001_initial.py # Migration file, will incremental
│ │ ├── __init__.py       # App init file
│ │ ├── admin.py          # Manages the integration with Django's admin site.
│ │ ├── forms.py          # Manages the function for form vaildation.
│ │ ├── apps.py           # Configures the app's settings and behavior.
│ │ ├── models.py         # All the models will migrated to the database tables.
│ │ ├── tests.py          # Test fo the app
│ │ ├── urls.py           # Define the URL routing for the app
└── └── views.py          # User define function called when get client request URL 
```

## Steps:
### Create new model if need to have validation data
* Starting a new app and add the app name to <project_lvl>/settings.py
    ```bash
    # start a app
    python manage.py startapp <name_of_app>
    ```
    ```python
    INSTALLED_APPS = [
    '...', # Other apps settings
    'name_of_app' # The name of the new app
    ]
    ```
* Adding the model info into the <new_app>/models.py if we need to save data to model.
    ```python
    # Create your models here.
    class Contact(models.Model):
        id = models.IntegerField() # Field for storing Int data
        name = models.CharField(max_length=200) # Field for storing Str data
        salary = models.FloatField() # Field for storing Float data
    ```
* Create <new_app>/forms.py file and start creating the form class.
    ```python
    # Import the class from the model if the data need to save to database
    # Else use forms.Form instead of forms.ModelForm 
    from .models import Contact
    # from django import forms

    class ContactForm(forms.ModelForm):
        class Meta:
            model = Contact
            # fields = "__all__"
            fields = ['id', 'name', 'salary']
    ```
* Import the form data to view.
    ```python
    class ContactFormView(View):
        # Default url
        template_name = 'contact_form.html'
        success_url = reverse_lazy('thank_you')
        failed_url = reverse_lazy('failed_to_load')
        def get(self, request, *args, *kargs):
            pass
        def post(self, request, *args, **kwargs):
            pass
    ```
* Update the <new_app>/urls.py and <project>/urls.py
    ```python
    urlpatterns = [
        path('contact/', ContactFormView.as_view(), name='contact_form') # For GET page,
        path('thank-you/', TemplateView.as_view(template_name='thank_you.html'), name='thank_you') # For success,
    ]
    ```

## Note & Mistakes