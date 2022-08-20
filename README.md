# Django-Ploty-Visualisation
Using ploty to visualise data from Django database 

Cleate a Repo

Clone the repo to your harddrive:
  a) Open a VS code,
  b) Go to clone git Repository,
  c) Copy the Repo adress and paste on VS code,
  d) Select the location on your harddrive and open on VS code.
  
Create a Python 3 Virtual environment:
  a)  python3 -m venv dpenv
  b)  source dpenv/bin/activate
 
pip install the following librarys into to Virtual env
    Django
    django-extensions
    plotly
    django-psycopg2
    django-decouple

Create Project:
    django-admin startproject visualisation

Change Directory into the project
    cd visualisation

Create app:
    python manage.py startapp dplotly

Open a new Terminal (SQL terminal)

Create a postgreSQL run the following codes on the new terminal:
    psql -U postgres
    enter the password
    CREATE DATABASE cryptocurrency;
    \c cryptocurrency

Close the SQL Terminal 

Goto Settings.py on your django code and update the following:
    INSTALLED_APPS[ add the 'dplotly' ]
    change the DATABASES to:

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'cryptocurrency',
                'USER': 'postgres',
                'PASSWORD': 'password',
                'HOST': 'localhost',
                'PORT': '',
            }
        }

    NAME        is the name of the database we created for our project'cryptocurrency'.
    USER        is the database user postgres.
    PASSWORD    is the password to the database.

Create .env for hiding passwords and other screat codes
    in the same directory as settings.py 
    create a file and name it .env
    copy and move your django secret code to .env file
    pip install python-decouple
    Replace with this config('SECRET_KEY')

Update the following codes on settings.py:
    import os
    from decouple import config
    import psycopg2
    from pathlib import Path

    SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))

Make Migrations

git add .
git commit -m 'first commit'
git push
