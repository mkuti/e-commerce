from django.shortcuts import render
from products.models import Product

def do_search(request):
    '''
    Search function where whatever typed into form will be used to filter the products
    '''
    products = Product.objects.filter()
    return render(request, 'products.html', {'products': products})
