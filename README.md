# Opportunity Network - Django Assignment
This repository contains the django project for the Django Assignment created by Opportunity Network.


#### Create a python environment and install the requirements
Run the following commands to create a python environment and install the project's requirements:
```
opnet-django-assignment$ virtualenv env
opnet-django-assignment$ source env/bin/activate
opnet-django-assignment$ pip install -r requirements.txt
```

#### Prepare database and create super  user
Run the following commands to prepare database and create a super user for Django admin site:
```
opnet-django-assignment/project$ python manage.py makemigrations
opnet-django-assignment/project$ python manage.py migrate
opnet-django-assignment/project$ python manage.py createsuperuser
```

#### Compile messages for Translations
Run the following command to compile the created messages:
```
opnet-django-assignment/project$ python manage.py compilemessages
```


#### Run Django server
Run the following command to run the server:
```
opnet-django-assignment/project$ python manage.py runserver
```

#### Server routes
The server has the following routes:

- Django admin site: `/admin`
- Published events page: `/events`
- Published event's detail page: `/events/{id}`

#### Run Tests
Run the following command to run the tests:
```
opnet-django-assignment/project$ python manage.py test events
```