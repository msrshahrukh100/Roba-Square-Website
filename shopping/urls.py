from django.conf.urls import include, url
from django.contrib import admin
from .views import view_category_or_item,search, view_private_item, show_private_item, checkavailability,bulkorders

urlpatterns = [

    url(r'^(?P<qtype>[\w-]+)/(?P<slug>[\w-]+)/$', view_category_or_item, name='view_category_or_item'),
    url(r'^customize/(?P<slug>[\w-]+)$', view_private_item, name='view_private_item'),
    url(r'^view/customizedproduct/(?P<slug>[\w-]+)/(?P<key>\d+)$', show_private_item, name='show_private_item'),
    url(r'^search/',search,name='search'),
    url(r'^checkavailability/',checkavailability,name='checkavailability'),
    url(r'^bulkorders/',bulkorders,name='bulkorders'),

]
