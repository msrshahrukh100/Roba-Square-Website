from django.conf.urls import include, url
from django.contrib import admin
from .views import viewinvoice

urlpatterns = [

    url(r'^viewinvoice/$', viewinvoice.as_view()),
    # url(r'^deletereview/(?P<id>\d+)$', deletereview, name='deletereview'),
    # url(r'^productsuggestion/$', productsuggestion, name='productsuggestion'),

]
