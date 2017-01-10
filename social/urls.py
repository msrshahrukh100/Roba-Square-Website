from django.conf.urls import include, url
from django.contrib import admin
from .views import (viewallusers, addconnection, removeconnection)

urlpatterns = [

    url(r'^viewallusers/$', viewallusers, name='viewallusers'),
    url(r'^addconnection/(?P<id>\d+)$', addconnection, name='addconnection'),
    url(r'^removeconnection/(?P<id>\d+)$', removeconnection, name='removeconnection'),
    
]
