from django.conf.urls import include, url
from django.contrib import admin
from .views import (viewallusers, addconnection, removeconnection, myprofile, viewuser, readallnotifications, likedislike,search,addpicofweek, viewpicofweek,showallnotifications,deletehistory)

urlpatterns = [

    url(r'^viewallusers/$', viewallusers, name='viewallusers'),
    url(r'^addconnection/(?P<id>\d+)$', addconnection, name='addconnection'),
    url(r'^removeconnection/(?P<id>\d+)$', removeconnection, name='removeconnection'),
    url(r'^myprofile/$', myprofile, name='myprofile'),
    url(r'^viewuser/(?P<slug>[\w-]+)$', viewuser, name='viewuser'),
    url(r'^readallnotifications/$', readallnotifications, name='readallnotifications'),
    url(r'^likedislike/(?P<id>\d+)$', likedislike, name='likedislike'),
    url(r'^search/',search,name='search'),
    url(r'^addpicofweek/',addpicofweek,name='addpicofweek'),
    url(r'^viewpicofweek/',viewpicofweek,name='viewpicofweek'),
    url(r'^showallnotifications/',showallnotifications,name='showallnotifications'),
    url(r'^deletehistory/',deletehistory,name='deletehistory'),
    
]
