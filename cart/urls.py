from django.conf.urls import include, url
from django.contrib import admin
from .views import addtocart

urlpatterns = [

    url(r'^addtocart/(?P<id>\d+)$', addtocart, name='addtocart'),
]
