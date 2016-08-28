from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
import settings
from catalog import views as catalog_views
from main import views as main_views


urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^$', main_views.main),
    url(r'^admin/', admin.site.urls),
    url(r'^catalog/', catalog_views.catalog),
    url(r'^product/(?P<product_slug>[a-zA-Z0-9-_.]+)/$', catalog_views.product),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
