# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from catalog.models import Product
from django.core.urlresolvers import reverse
import uuid


PAYMENT_TYPE = (
    ('Cash', u'Наличными'),
    ('Internet', u'Электронными'),
)

class Cart(models.Model):
    add_date = models.DateTimeField(u'Время добавления', auto_now_add=True)

    def __unicode__(self):
        return self.add_date.strftime('%Y-%m-%d   %H:%M:%S')

    class Meta:
        verbose_name = "корзина"
        verbose_name_plural = "Корзины"

    def total_price(self):
        result = 0
        for item in self.products_in_cart.all():
            result += item.product.price * item.quantity
        return result

    def get_products(self):
        return self.products_in_cart.all()

    get_products.short_description = 'Products'


class ProductInCart(models.Model):
    cart = models.ForeignKey(Cart, related_name='products_in_cart')

    product = models.ForeignKey(Product, verbose_name="Продукт")
    quantity = models.IntegerField(u'Количество', default=1)

    def __unicode__(self):
        return self.product.title

    class Meta:
        verbose_name = "продукты в корзине"
        verbose_name_plural = "Продукты в корзине"

    def cost_of_products(self):
        return self.product.price * self.quantity


class Order(models.Model):
    name = models.CharField(u'ФИО', max_length=64)
    phone = models.CharField(u'Номер телефона', max_length=11, help_text=u'Мы позвоним вам для уточнения заказа.')
    email = models.EmailField(u'Email', max_length=32, blank=True, null=True, help_text=u'Не обязательно, но мы туда пришлем данные о заказе.')
    isDelivery = models.BooleanField(u'Нужна ли доставка', default=False, help_text=u'Нужна ли доставка ?')
    address = models.CharField(u'Адрес', max_length=128, blank=True, null=True, help_text=u'Укажите адрес, для доставки')

    cart = models.ForeignKey(Cart, null=True, related_name='products')
    payment_type = models.CharField(u'Способ оплаты', max_length=30, choices=PAYMENT_TYPE, default=0, help_text=u'Выберите способ оплаты')
    price = models.IntegerField(u'Стоимость', editable=False)
    secret = models.CharField(max_length=60)
    add_date = models.DateTimeField(u'Дата оформления', auto_now_add=True)

    isAgreed = models.BooleanField(u'Согласовано', default=False)
    isPaid = models.BooleanField(u'Оплачено', default=False)
    isDelivered = models.BooleanField(u'Доставлено', default=False)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "заказы"
        verbose_name_plural = "Заказы"

    @staticmethod
    def get_random_id():
        return uuid.uuid1()

    def get_absolute_url(self):
        return reverse('order_item', args=[self.secret])