# Corner Case Task for Software Developer

This is the project developed for the Corner Case software developer role. It consists in a API for menu voting. For that specif version no authentication was implemented. However, the following action are covered:
* Create, edit, retrieve and delete Employees.
* Create, edit, retrieve and delete Restaurants.
* Create, edit, retrieve and delete Menus. 
  *  The menu supports "pdf" file upload when performing the create and update action.
  * A function for get all the menus for the current day is implemented.
  * A function for get all the menus for a specif day is implemented as well.
* Create, edit, retrieve and delete Votes.
  * A function responsible for get all the Votes for a specific day is implemented.

The system also has a logging function and a Django's built-in admin area that can be accessed by the following settings:
* Address: IP:PORT/admin (on dev: 127.0.0.1:8000/admin) 
* Username: admin
* Password: admin


## Requirements
In order to run this application is necessary meet the following requirements:
1. Python 3.x
2. Django 2.X
3. Django Rest

## Installation via pip

**Cloning project:**\
$git clone https://github.com/DaniloRodrigo/corner_case.git

**Installing requirements:**\
$ pip install django\
$ pip install djangorestframework

**Installing migration:**\
$ python manage.py migrate

> Note: You can also use virtualenv or anaconda to manage the development or production environment.

## Run project

Before start the project is necessary run the migrations to set the database 

### Unit Tests

$ python manage.py test

### Serve

$ python manage.py runserver

## Logging

The system implements a logging functionality that show messages on the console during the unit tests and also saves many important information on the "debug.log" file located on the log directory. 
