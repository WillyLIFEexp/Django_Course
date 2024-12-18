# Model pratice
## :closed_book: Project Directory Structure
```bash
Django_Course/
├── demo_models/          # App folder
│ │ ├── migrations/       # Migrations detail folder
│ │ │ ├── __init__.py     # Migrate init file
│ │ │ └── 0001_auto.py    # Models records
│ │ ├── __init__.py       # App init file
│ │ ├── admin.py          # Manages the integration with Django's admin site.
│ │ ├── apps.py           # Configures the app's settings and behavior.
│ │ ├── models.py         # All the models will migrated to the database tables.
│ │ ├── tests.py          # Test fo the app
│ │ ├── urls.py           # Define the URL routing for the app
└── └── views.py          # User define function called when get client request URL 
```

## Steps:
### Install DRF
* Starting a new app and install DRF library
    ```bash
    # start a app
    poetry add djangorestframework
    ```
### With basic method to using DRF.
    ```python
    from django.shortcuts import render
    from rest_framework.response import Response
    from rest_framework import status
    from rest_framework.decorators import api_view

    @api_view()
    def book(request):
        return Response('list of the books', status=status.HTTP_200_OK)
    ```

## Note & Mistakes