from django.conf.urls import include, url
from .views import viewinvoice, checkoutpage

urlpatterns = [

    url(r'^viewinvoice/$', viewinvoice.as_view()),
    url(r'^checkoutpage/$', checkoutpage, name='checkoutpage'),
]
