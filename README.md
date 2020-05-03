# E-COMMERCE MINI-PROJECT

An e-commerce website using Python as a language, Stripe too to allow both private individuals and businesses to accept payments, and AWS which cloud storage service will be used to store static and media files of the project. 

The website will display products, search for products, place products in a cart, register users and purchase products with a credit or debit card

## START PROJECT
1. pip3 install django==1.11.29
2. pip3 freeze > requirements.txt
3. django-admin startproject ecommerce .
4. Add 'localhost' under ALLOWED_HOSTS in settings.Python
5. Add *.sqlite* to .gitignore file 

## START FIRST APP FOR AUTHENTICATION 
1. re-use accounts app from previous project of django_authentication
2. download zip, unzip
3. create folder called "accounts" at root level and upload all files from accounts folder of zip download
4. create folder under accounts, called "templates" and upload 4 templates files
5. Create root folder called "templates" and upload base.html
6. create a folder under templates called "Registration" and upload all password_reset html templates
7. Create root folder called "static", add another folder called "css" and upload style.css
8. Add AUTHENTICATION_BACKENDS under settings.Python
>> AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'accounts.backends.EmailAuth'
]
9. at bottom of settings.py, add MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
10. check python3 manage.py makemigrations and python3 manage.py makemigrations accounts

## WIRE UP URLS TO APP
1. wire up the urls to accounts: url(r'^accounts/', include(urls_accounts))
2. Add include to import from django
3. from .accounts import urls as urls_accounts
4. pip3 install django-forms-bootstrap
5. python3 manage.py createsuperuser
6. add django_forms_bootstrap under INSTALLED_APPS in settings.py
7. Add os.path.join(BASE_DIR, 'templates') under templates, inside 'DIRS':[] in settings.py
>> all directories called templates potentially contain templates


