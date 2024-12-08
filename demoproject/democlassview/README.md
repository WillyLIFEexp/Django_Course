# Demo Class view
## :closed_book: Project Directory Structure
```bash
Django_Course/
├── democlassview/       # App folder
│ │ ├── migrations/      # Migrations detail folder
│ │ │ ├── __init__.py    # Migrate init file
│ │ ├── templates/       # Migrations detail folder
│ │ │ └── democlassview/ # Migrate init file
│ │ │ │ └── form.html    # User define function called when get client request URL 
│ │ ├── __init__.py   # App init file
│ │ ├── admin.py      # Manages the integration with Django's admin site.
│ │ ├── apps.py       # Configures the app's settings and behavior.
│ │ ├── models.py     # All the models will migrated to the database tables.
│ │ ├── tests.py      # Test fo the app
│ │ ├── urls.py       # Define the URL routing for the app
└── └── views.py      # User define function called when get client request URL 
```

## Steps: