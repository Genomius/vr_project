from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
import settings


urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^', include('main.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^catalog/', include('catalog.urls')),
    url(r'^cart/', include('cart.urls', namespace='cart')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
