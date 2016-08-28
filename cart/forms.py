from django.forms import ModelForm, HiddenInput
from models import Cart, ProductInCart, Order


class ProductInCartForm(ModelForm):
    class Meta:
        model = ProductInCart
        exclude = ['cart']


class OrderForm(ModelForm):
    class Meta:
        model = Order
        exclude = ["isAgreed", "secret", "cart", "isPaid", "isDelivered", "price"]
