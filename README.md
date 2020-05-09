# E-COMMERCE MINI-PROJECT

An e-commerce website using Python as a language, Stripe too to allow both private individuals and businesses to accept payments, and AWS which cloud storage service will be used to store static and media files of the project. 

The website will display products, search for products, place products in a cart, register users and purchase products with a credit or debit card

[![Build Status](https://travis-ci.org/mkuti/e-commerce.svg?branch=master)](https://travis-ci.org/mkuti/e-commerce)

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


## CREATE NEW APP CALLED HOME (ABOUT OR WELCOME)
1. django-admin startapp home or python3 manage.py startapp home
2. add app under INSTALLED_APPS in settings.py
3. add def index in views
4. create index.html template inside new folder templates

## CREATE PAGE FOR PRODUCTS
1. django-admin startapp products or python3 manage.py startapp products
2. add producs on the list of INSTALLED_APPS
2. in models.py, decide of the form fields for the products (see models.py) which will then be added to database
3. on admin.py, add from .models import Product and admin.site.register(Product)
4. do some tests of the models (see tests.py)
5. pip3 install pillow >> python package that allows images to be uploaded
6. pip3 freeze > requirements.txt
7. python3 manage.py makemigrations products
8. python3 manage.py migrate products
9. python3 manage.py test products

## PRODUCTS VIEWS AND URLS
1. in views, from .models import Product
2. add a function to display all products from the database and return the template
3. create new urls.py file inside products app
4. from django.conf.urls import url, include
5. from .views import all_products
6. create basic url(r'^$', ... ) named products
7. Create folder of templates within products app
8. Create products.html file
9. extends base.html and add block content
10. add for product in products loop within a row
11. add responsive bootstrap columns classes for a div
12. add another div with product class for image and add style="background-image: url('{{ MEDIA_URL }}{{ product.image }}')"
13. add product name in a h3
14. add product description inside p element with class product-description
15. add product price inside p element
16. add a form to allow user to select product and add to cart
17. form element and inside add method=POST, action=" {% url 'add_to_cart' product.id %}"
18. add {% csrf_token %}
19. inside div with class input-group, add input element to indicate quantity of product to be added to cart
20. inside a span with class of input-group-btn, add button with btn-success and type of submit

21. inside settings.py, under templates, add 'django.template.context_processors.media',
22. inside settings.py, at the bottom, add MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

23. in top-level urls, from products import urls as urls_products
24. from products.views import all_products
25. from django.views.static import serve
26. from .settings import MEDIA_ROOT
27. create base url(r'^$', all_products, name='index'),
28. create new url(r'^products/', include(urls_products))
29. add url for media: url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

## STORING SHOPPING CART ITEMS IN A SESSION 
1. django-admin startapp cart or python3 manage.py startapp cart
2. add app 'cart' under INSTALLED_APPS in settings.py
3. create a new file called "contexts.py'
>> cart items will not go into the database, just stored in the session when user is logged in
4. from django.shortcuts import get_object_or_404
5. from products.models import Product
6. def function cart_contents(request)
>> allow anything added to the cart to be displayed on any web page within web app
>> creating a context that's available to all pages
7. cart = request.session.get('cart', {})
>> request existing cart if there is one, or blank dictionary if none
8. initialise cart_items, total and product_count
9. create for loop: for id, quantity in cart.items():
>> 2 arguments: product ID, quantity of how many user wishes to purchase
10. product = get_object_or_404(Product model, primary key=id)
11. total: quantity of items multiplied by their price and add this to continuous running total of cost 
12. product_count just keeps on adding the quantity
13. append cart.items to the cart_items with id, quantity and product
14. return a dictionary {'cart_items: cart_items, 'total': total, 'product_count: product_count}

15. in settings.py, add 'cart.contexts.cart_contents' in TEMPLATES 
>> allow to have the context file always available on all templates
>> no need to pass them in views

16. create urls.py inside cart app
17. from django.conf.urls import url, include
18. from .views import view_cart, add_to_cart, adjust_cart
19. create base url to view cart
20. create url to add cart which takes product id added to the path: cart/add/id
21. create url to adjust cart which also takes product id added to the path: cart/adjust/id

22. in views.py, add redirect and reverse to list of import from django.shortcuts
23. create basic function to render cart contents
23. create 2nd view for add_to_cart which takes the product ID
24. quantity=int(request.POST.get('quantity')) >> allow us to increase or decrease the number of items we want
>> the integer chosen with the products.html form will go straight to the cart
25. cart = request.session.get('cart', {}) >> request cart from session, get an existing cart or an empty dict 
26. cart[id] = cart.get(id, quantity) >> add id and quantity to the cart
27. request.session['cart'] = cart >> save what has been added to the cart of the current session
28. return redirect(reverse('index'))
29. create 3rd view for adjust_cart which takes the product ID
30. quantity = int(request.POST.get('quantity')) >> existing quantity
31. cart = request.session.get('cart', {}) >> request cart from session, get an existing cart or an empty dict
32. if statement for quantity greater than 0, if nothing in the cart, cannot adjust it, cart.pop(id)
33. request.session['cart'] = cart >> save what has been added to the cart of the current session
34. return redirect(reverse('view_cart'))

35. add urls_cart to top-level urls

## CART WEBPAGE HTML 
1. create template in cart app
2. add cart.html inside
3. {% extends 'base.html' %}
4. {% load static from staticfiles %}
>> allows us access to anything in our static directory, so, for example, CSS, JavaScript, fonts, or anything we wish
5. {% block content %}
6. div of class row and row-flex
7. {% for item in cart_items %}
8. check main html structure in cart.html
9. add div outside loop for the total shown and the button to checkout
10. using glyphicon classes from bootstrap for small icon on buttons

## SEARCH 
1. django-admin startapp search
2. add search app in INSTALLED_APPS
3. in views.py, from products.models import Product
4. create function call do_search
5. products = Product.objects.filter(name__icontains=request.get[q])
>> will get whatever 'q' is returned from the form, so we'll give the form a name of 'q'
>> whatever typed into form will be used to filter the products
6. return render(request, 'products.html', {'products': products})
7. create base url named 'search'
8. link up to top-level urls under urls_search
10. in base.html, change title and heading to ecommerce
11. Add stylesheet link for font-awesome
11. add cart icon on the navbar with font-awesome icons and label to show product_count if above 0, with badges classes
12. add search form above block content with action to search url, method is get, and name of input is 'q'
13. add button inside the form to submit the search
14. in settings.py, add STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'))

## STRIPE API
1. pip3 install stripe 
2. go to stripe.com 
3. Start account
4. Go to test api keys
5. click on eye next to secret key to reveal the key
6. copy the key
7. in settings.py at the bottom, add STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE')
STRIPE_SECRET = os.getenv('STRIPE_SECRET')
8. create new file env.py at root level
9. import os
10. os.environ.setdefault('STRIPE_PUBLISHABLE', '')
11. same for STRIPE_SECRET
12. add env.py into .gitignore: echo env.py >> .gitignore
13. import env inside settings

## CREATE CHECKOUT APP
1. django-admin startapp checkout
2. add checkout app to settings.py INSTALLED_APPS
3. go to models.py
4. from products.models import Product
5. create class Order(models.Model):
6. full_name, phone_number, country, postcode, town_or_city, street_address1, street_address2, county, date
7. all use CharField and set blank=False which means the field cannot be left blank
8. use DateField() for date
9. see follow up in checkout/models.py
10. add new models inside admin.py of the app > so we can edit them via admin panel
11. from .models import Order, OrderLineItem
11. admin.site.register(Order, OrderAdmin)
12. 2 classes created for some reason 
13. python3 manage.py makemigrations checkout
14. python3 manage.py migrate checkout

## CHECKOUT FORMS 
1. Create forms.py inside checkout app
2. from django import forms
3. from .models import Order
4. Create a Payment form
5. Create an order form based on the model previously created

## CHECKOUT VIEWS 
1. in views.py, do all following imports
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
import stripe
2. stripe_api_key = settings.STRIPE_SECRET
3. @login_required before the function to only allow customers here when logged in
4. all following described in comment of views.py

## CHECKOUT URLS AND HTML
1. Create new urls.py file inside checkout app
2. from django.conf.urls import url
3. from .views import check_out
4. base url which is wired up with check_out view and with name check_out
5. add checkout urls to top-level urls
6. create new html template for checkout inside new folder called templates
7. Add {% block head_js %} {% endblock head_js %} below scripts inside base.html so that js script from checkout will only be injected into base.html when user click on checkout
8. Add {% extends 'base.html' %}, {% load static from staticfiles %}, {% load bootstrap_tags %}
9. {% block head_js %} {% endblock %}
10. in that block, add <script type="text/javascript" src="https://js.stripe.com/v2/"></script>
>> direct link to Stripe js
11. add the. <script type="text/javascript">
    //<![CDATA[
        Stripe.publishableKey = '{{ publishable }}';
        //]]>
</script>
>> to set the stripe publishable key
12. add <script type="text/javascript" src=" {% static 'js/stripe.js' %} "></script>
>> will create file afterwards
13. added same html as cart to display product within the loop for item in cart_items
14. below show total
15. add a form within which we'll display the legend called payment details
16. before the actual form, a space for messages to display messages after payment submitted
17. using |as_bootstrap, integrate order_form and payment_form
18. add a button to submit the payment

## CREATE HEROKU APP
1. add os.environ.setdefault('SECRET_KEY', 'secret-key-here') in env.py
2. in settings.py, add >> SECRET_KEY = os.environ.get('SECRET_KEY')
3. Create app in Europe on heroku dashboard
4. Add add-ons, Heroku Postgres database
5. Add SECRET_KEY environment variable on heroku settings
6. On terminal, pip3 install dj-database-url psycopg2
7. pip3 freeze > requirements.txt
8. Update settings.py to use new database url
9. comment out default databases
10. add DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}
11. import dj_database_url
12. Add database url in env.py for running app locally, copy and paste database_url from heroku
13. os.environ.setdefault('DATABASE_URL', 'add_database_url_here')
14. python3 manage.py migrate to move all tables to new heroku database
15. python3 manage.py createsuperuser

## USE AWS S3
1. Once on AWS dashboard, search for S3 
2. Buckets are the fundamental container in Amazon S3 for data storage.
3. Create a bucket 
>> makes it public for the purpose of using the bucket to host a static website
4. go to properties
5. go to static website hosting
6. tick use this bucket to host a website
7. add index.html in index and error.html for error
8. save
9. go to permissions
10. go to CORS configuration and add
<CORSConfiguration>
<CORSRule>
<AllowedOrigin>*</AllowedOrigin>
<AllowedMethod>GET</AllowedMethod>
<MaxAgeSeconds>3000</MaxAgeSeconds>
<AllowedHeader>Authorization</AllowedHeader>
</CORSRule>
</CORSConfiguration>
11. go to policy
>>  bucket policy is what allows access to the contents of a bucket from any website across the web
12. add {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::mapi-ecommerce/*"
            ]
        }
    ]
}
13. search in AWS dashboard or services tab for IAM 
>> Identity and Access Management to manage who access our AWS
14. on IAM dashboard, go to groups
15. create a group called mapi-ecommerce-group
16. click next twice and create group
17. go to policies of IAM and create one
>> A policy defines the AWS permissions that you can assign to a user, group, or role. You can create and edit a policy in the visual editor and using JSON. 
18. import managed policy, search for S3 and import S3FullAccess
19. in JSON file, add ["arn:aws:s3:::mapi-ecommerce", "arn:aws:s3:::mapi-ecommerce/*"] inside resource
20. click on review policy
21. give a name and create policy
22. go back to groups and open the group created before
23. go to permissions and attach policy just created
24. go to users and create a user called mapi-ecommerce-user
25. give programmatic access
26. add permissions of the group
27. click on next twice and create
28. download csv file
>> This is the access keys that you will need in your software. It's important to keep them safe. You'll never be able to generate them again. So if you lose them you would have to delete the user and create a new user with new access keys.
29. click done 
30. go back to S3 and try to upload an image
31. after uploading, if we click on image, we can see the object url accessible from anywhere in the web

## LINK S3 TO DJANGO 
1. pip3 install django-storages
2. pip2 install boto3
3. add storages as INSTALLED_APPS in settings.py 
4. at the bottom before STATIC, add following
AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000'
}
>> Static files tend not to change that many things, like CSS, so browsers will often cache them.
So the first thing that we're going to add in here is just something to allow boto to know that it can cache the static files.So we're putting in an expiry date here.
5. after that, add following
AWS_STORAGE_BUCKET_NAME = 'name-bucket'
AWS_S3_REGION_NAME = 'eu-west-1'
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
6. add following in env.py
os.environ.setdefault('AWS_ACCESS_KEY_ID', 'id_here')
os.environ.setdefault('AWS_SECRET_ACCESS_KEY', 'secret_key_here')
>> These keys are particularly important to keep secret because if somebody got hold of these, they could put terabytes worth of data through your S3 bucket at your expense.
7. python3 manage.py collectstatic

## ADDING MEDIA TO S3 
>> Enables S3 bucket subdirectories
>> Moves static files into their own subdirectory and changes standard image file storage to a S3 bucket subdirectory
>> Static content in one directory in S3 and media content, such as product images, on another.
1. Create new file at root level called custom_storages.py
2. from django.conf import settings
3. from storages.backends.s3boto3 import S3Boto3Storage
4. create class inheriting S3Boto3Storage
5. inside class, declare location = settings.STATICFILES_LOCATION
6. in settings.py, STATICFILES_LOCATION = 'static'
>> anything in a directory called static, which is our static files, will be part of that class
7. in settings.py, also change STATICFILES_STORAGE = 'custom_storages.StaticStorage', class just created
8. python3 manage.py collectstatic
>> collect all static again, copying them and putting them into static directory of S3 bucket
9. copy class for static storage and do the same for media storage to create a different directory
10. change new class to MediaStorage
11. in settings.py, add MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
12. in CORS configuration of S3 Bucket, add <AllowedMethod>HEAD</AllowedMethod> below the normal <AllowedMethod>GET</AllowedMethod>
13. change MEDIA_URL = '/media/' to "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)


add static/, media/, *.png to .gitignore

## SET UP TRAVIS CONTINUATION
1. click + next to current repository
2. click on switch to link up to new repository
3. go to build unknown, change format to markdown and copy text for README
4. paste it inside README
5. at root level, create new file called .travis.yml
6. add language: python
python:
- "3.4"
install: "pip install -r requirements.txt"
script:
- SECRET_KEY="whatever" ./manage.py test
7. after testing, > some errors
8. changed version of pillow to latest version known to travis
9. comment out env inside settings.py as running it from heroku in production
10. Travis testing wont know the database url
11. if 'DATABASE_URL' in os.environ: > >> use Heroku database stored in env.py
12 else, use sqlite3 database, copy the commented out DATABASES before
>> if DATABASE_URL is in our environment, then we use it, if not, then we use SQLite instead which is already uploaded to github