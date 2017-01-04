from django.conf.urls import include, url
from django.contrib import admin
from .views import home_page, change_settings

urlpatterns = [

    url(r'^$', home_page, name='homepage'),
    url(r'^change_settings/$', change_settings, name='change_settings'),
]
