from django import forms
from .models import Order


class MakePaymentForm(forms.Form):
    '''
    Create payment form to input credit card number
    First create choice fields for month and year expiry date
    required=False is to hide plain text and
    let Stripe encrypt card, as more secure
    stripe_id is created automatically and hidden from customer
    '''
    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2017, 2036)]

    credit_card_number = forms.CharField(
        label='Credit card number',
        required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(
        label='Month',
        choices=MONTH_CHOICES,
        required=False)
    expiry_year = forms.ChoiceField(
        label='Year',
        choices=YEAR_CHOICES,
        required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):
    '''
    Order Form inheriting from the model previously created
    Adding the Meta class required for models
    Specifying the fields where customer need to enter information
    '''
    class Meta:
        model = Order
        fields = (
            'full_name',
            'phone_number',
            'country',
            'postcode',
            'town_or_city',
            'street_address1',
            'street_address2',
            'county')
