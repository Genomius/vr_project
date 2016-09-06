from django.conf.urls import url
import views


urlpatterns = [
    url(r'^$', views.catalog, name='catalog'),
    url(r'^(?P<product_slug>[a-zA-Z0-9-_.]+)$', views.product, name='product'),
]