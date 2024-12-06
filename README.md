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
├── demoapp/      # Project folder
│ │ ├── migrations/    # App folder
│ │ │ ├── __init__.py   # App init file
│ │ ├── __init__.py   # App init file
│ │ ├── admin.py       # For asynchronous web applications
│ │ ├── apps.py       # For asynchronous web applications
│ │ ├── models.py     # All the models will migrated to the database tables.
│ │ ├── tests.py      # Test fo the app
│ │ ├── urls.py       # URL mapping mechanism
│ │ └── views.py      # User define function called when get client request URL 
│ ├── demoproject/    # App folder
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

<!-- ## :wrench: Setting up

* Clone the Repo
* Build the container using the following command.
    ```
    docker build -t flask_docker .
    ```
* Starting the container with port mapping and let container to run in the background.
    ```
    docker run -d -p 5000:5000 flask_docker
    ```
* Stop the container by using the following command.
    ```
    docker stop <container-id-or-name>
    ``` -->

<!-- ## :pencil2: Testing
* Enter the container by the following command.
    ```
    docker exec -it <container-id-or-name> bash
    ```
* Running pytest to check for result
    ```
    pytest tests/test_hello.py
    ``` -->

## TO-DO