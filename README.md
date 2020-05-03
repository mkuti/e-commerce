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

16. create urls.py inside cart app
17. from django.conf.urls import url, include
18. from .views import view_cart, add_to_cart, adjust_cart
19. create base url to view cart
20. create url to add cart which takes product id added to the path: add/id
21. create url to adjust cart which also takes product id added to the path: adjust/id

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

