# Django_Course
This will the note for me when learning about Django

## :hammer_and_pick: Technologies Used
- **Language**: Python
- **Backend Framework**: Django
- **Testing Framework**: Pytest
- **Containerization**: Docker

## :gear: Prerequisites
- Python 3.8+
- [Docker](https://docs.docker.com/engine/install/) 

## :closed_book: Project Directory Structure
```bash
Django_Course/
├── demoapp/          # Project folder
│ ├── demoapp/        # Basic app example
│ ├── democlassview/  # Class view example
│ ├── demo_models/    # Models example
│ ├── demoproject/    # Project and App general settings
│ │ ├── __init__.py   # App init file
│ │ ├── asgi.py       # For asynchronous web applications
│ │ ├── settings.py   # Config specific parameters with default values
│ │ ├── urls.py       # Routes and view mapping list
│ │ └── wsgi.py       # The engry point for such WSGI-compatible servers to serve classical web application 
│ └── manage.py       # Code the can perform django-admin 
├── Dockerfile        # Docker configuration file 
├── poetry.lock       # Records the exact versions of all dependencies 
├── pyproject.toml    # Project configuration file
└── README.md         # Documentation for the project
```

## Note:
```bash
# start a app
python manage.py startapp <name_of_app>

# Make migrations
# This refers to generating a database table whose structure matches the data model declared in the app
python manage.py makemigrations # new model is declared
python manage.py migrate # sync the database state with currently declared models and migrations

# Running server
python manage.py runserver

# Shell env, useful if need to perform some quick interactive operations
python manage.py shell
```

## Other README.md
* [Basic app](https://github.com/WillyLIFEexp/Django_Course/blob/first_check/demoproject/demoapp/README.md)
* [Classview app example](https://github.com/WillyLIFEexp/Django_Course/blob/first_check/demoproject/democlassview/README.md)
* [Model app example](https://github.com/WillyLIFEexp/Django_Course/blob/first_check/demoproject/demo_models/README.md)
