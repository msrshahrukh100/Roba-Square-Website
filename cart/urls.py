from django.conf.urls import include, url
from django.contrib import admin
from .views import (addtocart, addtowishlist, viewcart, deletefromcart, viewwishlist, deletefromwishlist)

urlpatterns = [

    url(r'^addtocart/(?P<id>\d+)$', addtocart, name='addtocart'),
    url(r'^deletefromcart/(?P<id>\d+)$', deletefromcart, name='deletefromcart'),
    url(r'^deletefromwishlist/(?P<id>\d+)$', deletefromwishlist, name='deletefromwishlist'),
    url(r'^addtowishlist/(?P<id>\d+)$', addtowishlist, name='addtowishlist'),
    url(r'^viewcart/$', viewcart, name='viewcart'),
    url(r'^viewwishlist/$', viewwishlist, name='viewwishlist'),
]
