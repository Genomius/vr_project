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
    url(r'^thanks/(?P<order_id>[0-9]+)/$', views.thanks, name='thanks'),
    # Страница с детализацией заказа
    url(r'^order/(?P<secret>[\w-]+)/$', views.order_detail, name='order_item'),
]
