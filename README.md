# My First Django Project

Polls app from official Django Tutorials
Django version 2.0.3
python version 3.6.4 Anaconda Distribution

Start Django project

``django-admin startproject mysite``

Run server

``python manage.py runserver``

To create your app, make sure you’re in the same directory as manage.py and type this command:

``python manage.py startapp api``

Some of these applications make use of at least one database table, though, so we need to create the tables in the database before we can use them. To do that, run the following command:

``python manage.py migrate``

The migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables according to the database settings in your project/settings.py

To include the app in our project, we need to add a reference to its configuration class in the INSTALLED_APPS setting. The ApiConfig class is in the api/apps.py file, so its dotted path is 'api.apps.ApiConfig'. Edit the mysite/settings.py file and add that dotted path to the INSTALLED_APPS setting. It’ll look like this:

    INSTALLED_APPS = [
        'api.apps.ApiConfig',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]

Now Django knows to include the api app. Let’s run another command:

``python manage.py makemigrations api``

By running **makemigrations**, you’re telling Django that you’ve made some changes to your models (in this case, you’ve made new ones) and that you’d like the changes to be stored as a migration.

Migrations are how Django stores changes to your models (and thus your database schema) - they’re just files on disk. You can read the migration for your new model if you like; it’s the file **api/migrations/0001_initial.py**

 The **sqlmigrate** command takes migration names and returns their SQL:

``python manage.py sqlmigrate api 0001``

The **migrate** command takes all the migrations that haven’t been applied (Django tracks which ones are applied using a special table in your database called django_migrations) and runs them against your database - essentially, synchronizing the changes you made to your models with the schema in the database.

``python manage.py migrate``

Interactive Python shell and play around with the free API Django gives you. To invoke the Python shell, use this command:

``python manage.py shell``

For more details about playing th Django API refer to:

[https://docs.djangoproject.com/en/2.0/intro/tutorial02/#playing-with-the-api](https://docs.djangoproject.com/en/2.0/intro/tutorial02/#playing-with-the-api)

## Admin Site

Creating an admin user¶

First we’ll need to create a user who can login to the admin site. Run the following command:

``python manage.py createsuperuser``

## Writing Views and Render HTML Pages

Refer to:

[https://docs.djangoproject.com/en/2.0/intro/tutorial03/](https://docs.djangoproject.com/en/2.0/intro/tutorial03/)

Refactor views.py and urls.py to use Django Generic/ Class Based Views
Refer to:

<https://docs.djangoproject.com/en/2.0/intro/tutorial04/#use-generic-views-less-code-is-better>

## Automated Testing

Testing for models and views in api/tests.py

``python manage.py test api``
