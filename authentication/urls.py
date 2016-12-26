from django.conf.urls import include, url
from django.contrib import admin
from .views import home_page

urlpatterns = [

    url(r'^$', home_page, name='homepage'),
]
