from django.conf.urls import url
import views


urlpatterns = [
    'main.views',
    url(r'^$/', views.main, name='main'),
]



