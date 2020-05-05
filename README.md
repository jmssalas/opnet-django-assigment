# Opportunity Network - Django Assigment
This repository contains the django project for the Django Assigment created by Opportunity Network.


#### Create a python environment and install the requirements
Run the following commands to create a python environment and install the project's requirements:
```shell script
opnet-django-assigment$ virtualenv env
opnet-django-assigment$ source env/bin/activate
opnet-django-assigment$ pip install -r requirements.txt
```

#### Prepare database and create super  user
Run the following commands to prepare database and create a super user for Django admin site:
```shell script
opnet-django-assigment/project$ python manage.py makemigrations
opnet-django-assigment/project$ python manage.py migrate
opnet-django-assigment/project$ python manage.py createsuperuser
```

#### Compile messages for Translations
Run the following command to compile the created messages:
```shell script
opnet-django-assigment/project$ python manage.py compilemessages
```


#### Run Django server
Run the following command to run the server:
```shell script
opnet-django-assigment/project$ python manage.py runserver
```

#### Server routes
The server has the following routes:

- Django admin site: `/admin`
- Published events page: `/events`
- Published event's detail page: `/events/{id}`

#### Run Tests
Run the following command to run the tests:
```shell script
opnet-django-assigment/project$ python manage.py test events
```