Getting started with python

1) Create a repostory
  for installing project specific requirement create a virtual environment
    python-m venv venv

2) Activate the virtual environment
  for windows: venv/scripts/activate
  for Mac/Linux: source venv/bin/activate

3) Now setup is complete
  install the required packages in virtual environment
    pip install Django

4) Create Django Project
    django-admin startproject core .

5) Run the Django project
    python manage.py runserver

6) Git Add/ Commit/ Push Commands
  git add .
  git commit -m "Your Commit Message"
  git push origin main

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydb',
        'USER': 'root',
        'PASSWORD': 'admin',
        'HOST':'localhost',
        'PORT':'3306',
    }
}

7.
     .\venv\Scripts\activate 
     cd core
     python manage.py runserver
     pip install Pillow
     python manage.py makemgirations
     python manage.py migrate
     python manage.py createsuperuser
     
     python manage.py runserver click ctrl+link in terminal or type localhost:8000/admin

     go to admin.py, then import.
    make product app



      