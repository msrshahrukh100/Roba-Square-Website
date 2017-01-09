from django.conf.urls import include, url
from django.contrib import admin
from .views import addreview, deletereview, productsuggestion

urlpatterns = [

    url(r'^addreview/$', addreview, name='addreview'),
    url(r'^deletereview/(?P<id>\d+)$', deletereview, name='deletereview'),
    url(r'^productsuggestion/$', productsuggestion, name='productsuggestion'),

]
