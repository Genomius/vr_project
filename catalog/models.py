# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from sorl.thumbnail import get_thumbnail
from importlib import import_module


def get_product_image_path(instance, filename):
    return 'products/%s/%s' % (instance.slug, filename)


def get_product_image_image_path(instance, filename):
    return 'products/%s/%s' % (instance.product.slug, filename)


class Product(models.Model):
    title = models.CharField(u'Наименование', max_length=64)
    description = models.TextField(u'Описание', max_length=4096)
    image = models.ImageField(u'Изображение', upload_to=get_product_image_path, blank=True, null=True)
    price = models.IntegerField(u'Стоимость')
    in_stoke_count = models.IntegerField(u'В наличии', default=0, help_text=u'сколько осталось на складе')

    sales_count = models.IntegerField(u'Продано', default=0, editable=False)
    returned = models.IntegerField(u'Возвращено', default=0, editable=False)
    slug = models.SlugField(u'URL', unique=True)
    add_date = models.DateField(u'Дата добавления', auto_now_add=True)

    @staticmethod
    def get_sales_count():
        summ = 0
        for product in Product.objects.all():
            summ += product.sales_count
        return summ

    @staticmethod
    def get_in_stoke_count():
        summ = 0
        for product in Product.objects.all():
            summ += product.in_stoke_count
        return summ

    def get_thumb_image(self):
        resize_img = get_thumbnail(self.image, '114x86', crop='center')
        return resize_img.url

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'продукт'
        verbose_name_plural = u'Продукт'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='product_image', verbose_name="Продукт")
    image = models.ImageField(u'Изображения', upload_to=get_product_image_image_path)

    def get_main_image(self):
        resize_img = get_thumbnail(self.image, '500x375', crop='center')
        return resize_img

    def get_thumb_image(self):
        resize_img = get_thumbnail(self.image, '114x86', crop='center')
        return resize_img

    class Meta:
        verbose_name = "изображение"
        verbose_name_plural = "Изображения"