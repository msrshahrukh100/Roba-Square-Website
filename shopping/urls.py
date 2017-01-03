from django.conf.urls import include, url
from django.contrib import admin
from .views import view_category_or_item

urlpatterns = [

    url(r'^(?P<qtype>[\w-]+)/(?P<slug>[\w-]+)/$', view_category_or_item, name='view_category_or_item'),
]