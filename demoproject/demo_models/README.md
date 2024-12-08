# Model pratice
## :closed_book: Project Directory Structure
```bash
Django_Course/
├── demo_models/          # App folder
│ │ ├── migrations/       # Migrations detail folder
│ │ │ ├── __init__.py     # Migrate init file
│ │ │ ├── 0001_initial.py # Migration file, will incremental
│ │ │ └── 0002_auto.py    # Alter models records
│ │ ├── __init__.py       # App init file
│ │ ├── admin.py          # Manages the integration with Django's admin site.
│ │ ├── apps.py           # Configures the app's settings and behavior.
│ │ ├── models.py         # All the models will migrated to the database tables.
│ │ ├── tests.py          # Test fo the app
│ │ ├── urls.py           # Define the URL routing for the app
└── └── views.py          # User define function called when get client request URL 
```

## Steps:
### Create new models
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
* Adding the model info into the <new_app>/models.py
    ```python
    # Create your models here.
    class Items(models.Model):
        id = models.IntegerField() # Field for storing Int data
        name = models.CharField(max_length=200) # Field for storing Str data
        price = models.FloatField() # Field for storing Float data
    ```
* Create new migration files based on changes made to our models, These migration files are Python scripts that describe how to modify the database schema to match the current state.
    ```python
    python manage.py makemigrations
    ```
* Excute the SQL in the migration files.
    ```python
    python manage.py migrate
    ```
### Update models
* Update the field on the models.py
* Check for the changes with makemigration
    ```python
    python manage.py makemigrations
    ```
    ```bash
    (venv) bash-3.2$ python manage.py makemigrations
    Migrations for 'demo_models':
        demo_models/migrations/0002_alter_items_name.py
            ~ Alter field name on items
    ```
* Excute the changes
    ```bash
    python manage.py migrate
    ```
### Remove models
* Remove the class inside the models.py
* Check for the changes with makemigration
* Excute the changes

### Check for migration history
* By using the following command to find the migrate history
*  [X] <- Finished executing
*  [ ] <- Haven't execute
    ```bash
    python manage.py showmigrations
    ```
### Preview the raw SQL
* By using the following command to preview the raw SQL that a migration will execute on the database. 
    ```bash
    python manage.py sqlmigrate <app_name> <migration_name> 
    ```
### Edit in AdminPage
* Update admin.py under the app.
```python
from django.contrib import admin
from .models import Items

# Register your models here.
admin.site.register(Items)
```

## Note & Mistakes