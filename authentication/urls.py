from django.conf.urls import include, url
from django.contrib import admin
from .views import (home_page, change_settings, change_dp, change_privacy_settings, addaddress, removeaddress, viewextra)

urlpatterns = [

    url(r'^$', home_page, name='homepage'),
    url(r'^change_settings/$', change_settings, name='change_settings'),
    url(r'^change_dp/$', change_dp, name='change_dp'),
    url(r'^change_privacy_settings/$', change_privacy_settings, name='change_privacy_settings'),
    url(r'^addaddress/$', addaddress, name='addaddress'),
    url(r'^removeaddress/(?P<id>\d+)$', removeaddress, name='removeaddress'),
    url(r'^terms/(?P<id>\d+)$', viewextra, name='viewextra'),

]
