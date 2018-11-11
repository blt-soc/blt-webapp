# blt-webapp

## About the project
add description later

## Requirements
* Python 3.5 or higher

## Setup and customize

1. `touch .env` To create an enviornment file, here is an example of what values must be filled.

```
DEBUG=true
SECRET_KEY=[secret-key]
DJANGO_SETTINGS_MODULE=django_config.settings.local
ALLOWED_HOSTS=localhost,127.0.0.1, 0.0.0.0
DATABASE_URL=postgres://[user]:[password]@[ip or localhost]:5432/[database]

POSTGRES_PASSWORD=[password]
POSTGRES_USER=[user]
POSTGRES_DB=[database]

```

2. Head over to the requirements folder and run
```
pip install -r local.txt
```
to install all local dependencies for the project

3. Run the basic django commands such as
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
