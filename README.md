# Zap

## Create Virtualenv with Python3 in Linux, Ubuntu or MAC
	virtualenv virtual/zap -p python3

## Create Virtualenv with Python3 in Windows
	python -m venv virtual\zap

## Activate Virtualenv in Linux, Ubuntu or MAC
	source virtual/zap/bin/activate

## Activate Virtualenv in Windows
	. virtual\zap\Scripts\activate

## Install Django and all Modules with pip3
	pip3 install django
	django-admin startproject zap
	django-admin startproject zap .
	pip3 install Pillow
	pip3 install djangorestframework
	pip3 install django-rest-auth
	pip3 install django-cors-headers
	pip3 install django-filter
	pip3 install mysqlclient
	LDFLAGS=-L/usr/local/opt/openssl/lib pip install mysqlclient

## Update requirements.txt file
	pip3 freeze > requirements.txt

## Start New Project in Django
	django-admin startproject zap

## Create New App in Django
	python manage.py startapp home

## Run Django
	python manage.py runserver
	python manage.py runserver 8080
	python manage.py runserver 0:8000
	python manage.py runserver 192.168.1.4:8000

## Create Superuser
	python manage.py createsuperuser

## Reset user Password from Terminal
	python manage.py changepassword username

## Makemigrations of Project or Single App
	python manage.py makemigrations
	python manage.py makemigrations home

## Migrate Project or Single App
	python manage.py migrate
	python manage.py migrate home
	python manage.py migrate --fake
	python manage.py migrate home --fake

## Run on Production Server
	python manage.py runserver

## Static files on Production Server
	python manage.py collectstatic
	python manage.py collectstatic --noinput
	python manage.py collectstatic --noinput --clear


## Install and Setup Redis Channel Layer for Message sent and recive
Before install channels_redis we need to install Redis server with Docker or Direct on our server and run it before using
We will use a channel layer that uses Redis as its backing store. To start a Redis server with Docker on port 6379, run the following command:

	docker run -p 6379:6379 -d redis:2.8

For Mac you can Install and Start Redis by these Commands and also check redis info
	
	brew install redis
	brew services start redis
	brew info redis

For Ubuntu you can Install and Start Redis Server by these commands and also check redis info

	sudo apt install redis-server
	sudo systemctl status redis
	sudo systemctl restart redis.service

After Running Redis Server you can Install redis for Channels with This Command

	pip3 install channels_redis

# Heroku Setup

## Install the Heroku CLI
Download and install the Heroku CLI.

If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key.

	$ heroku login

## Create Heroku Project
	heroku create zap

## Add Heroku Setting a buildpack on an application
	heroku buildpacks:set heroku/python

## You may also specify a buildpack during app creation
	heroku create zap --buildpack heroku/python

## Check Git Version and Initialize Git repo
	git --version
	git init

## Add Heroku settings in Current repo
	heroku git:remote -a zap

## Configuring Django Apps for Heroku with 'Procfile' to add this code
	web: gunicorn zap.wsgi

## Install gunicorn and django-heroku for Hosting
	pip3 install gunicorn
	pip3 install django-heroku

## Import django_heroku at top of Setting file and locals settings at Botton
	import django_heroku
	django_heroku.settings(locals())

## Follow this Link for More details
	https://devcenter.heroku.com/articles/django-app-configuration

## Set DJANGO_SETTINGS_MODULE env in wsgi file to heroku
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zap.settings.heroku')

## Push and Deploy the code on Heroku
	pip3 freeze > requirements.txt
	git status
	git add .
	git commit -m "Project Initial Setup"
	git push heroku master

## If we got static files related error then we need to disable it
	heroku config:set DISABLE_COLLECTSTATIC=1

## Access Heroku Bash run migrations commands
	heroku run bash
	python3 manage.py migrate
	python3 manage.py createsuperuser

## Check Logs if we got any error
	heroku logs --tail

### Thanks for Reading... ###
# Happy Coading!!! #
