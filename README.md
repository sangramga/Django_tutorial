# My First Django Project

Polls app from official Django Tutorials
Django version 2.0.3
python version 3.6.4 Anaconda Distribution

Start Django project

``django-admin startproject mysite``

Run server

``python manage.py runserver``

To create your app, make sure you’re in the same directory as manage.py and type this command:

``python manage.py startapp polls``

Some of these applications make use of at least one database table, though, so we need to create the tables in the database before we can use them. To do that, run the following command:

``python manage.py migrate``

The migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables according to the database settings in your project/settings.py

To include the app in our project, we need to add a reference to its configuration class in the INSTALLED_APPS setting. The PollsConfig class is in the polls/apps.py file, so its dotted path is 'polls.apps.PollsConfig'. Edit the mysite/settings.py file and add that dotted path to the INSTALLED_APPS setting. It’ll look like this:

    INSTALLED_APPS = [\
        'polls.apps.PollsConfig',\
        'django.contrib.admin',\
        'django.contrib.auth',\
        'django.contrib.contenttypes',\
        'django.contrib.sessions',\
        'django.contrib.messages',\
        'django.contrib.staticfiles',\
    ]\