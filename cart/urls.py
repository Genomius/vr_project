# coding: utf-8
from django.conf.urls import url
import views


urlpatterns = [
    # Страница корзины
    url(r'^$', views.cart, name='cart'),
    # Страница добавления товара
    url(r'^add/$', views.add, name='add'),
    # Страница удаления товара
    url(r'^remove/$', views.remove, name='remove'),
    # Страница оплаты
    url(r'^order/$', views.order, name='order'),
    # Страница благодарности
    url(r'^thanks/(?P<secret>[\w-]+)/$', views.thanks, name='thanks'),
    # Страница с детализацией заказа
    url(r'^order/(?P<secret>[\w-]+)/$', views.order_item, name='order_item'),
]
