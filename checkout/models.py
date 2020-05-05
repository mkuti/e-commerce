from django.db import models
from products.models import Product


class Order(models.Model):
    '''
    All the fields required 
    from a customer which will go into database
    '''
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=True)
    county = models.CharField(max_length=40, blank=False)
    date = models.DateField()

    def __str__(self):
        '''
        Returns summary of the order
        format injecting information into a string
        '''
        return "{0}-{1}-{2}". format(self.id, self.date, self.full_name)


class OrderLineItem(models.Model):
    '''
    Creates a new table/model
    including the order information from model above
    including the product information from model imported from products.models
    including the quantity
    '''
    order = models.ForeignKey(Order, null=False)
    product = models.ForeignKey(Product, null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        '''
        Returns the quantity of products being bought,
        the product name and product price
        '''
        return "{0} {1} @ {2}".format(
            self.quantity,
            self.product.name,
            self.product.price)
