from django.conf.urls import include, url
from django.contrib import admin
from .views import (viewallusers, addconnection, removeconnection, myprofile, viewuser)

urlpatterns = [

    url(r'^viewallusers/$', viewallusers, name='viewallusers'),
    url(r'^addconnection/(?P<id>\d+)$', addconnection, name='addconnection'),
    url(r'^removeconnection/(?P<id>\d+)$', removeconnection, name='removeconnection'),
    url(r'^myprofile/$', myprofile, name='myprofile'),
    url(r'^viewuser/(?P<slug>[\w-]+)$', viewuser, name='viewuser'),

    
]