from django.conf.urls import include, url
from django.contrib import admin
from .views import addtocart, addtowishlist, viewcart, deletefromcart

urlpatterns = [

    url(r'^addtocart/(?P<id>\d+)$', addtocart, name='addtocart'),
    url(r'^deletefromcart/(?P<id>\d+)$', deletefromcart, name='deletefromcart'),
    url(r'^addtowishlist/(?P<id>\d+)$', addtowishlist, name='addtowishlist'),
    url(r'^viewcart/$', viewcart, name='viewcart'),

]
