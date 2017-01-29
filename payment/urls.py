from django.conf.urls import include, url
from .views import viewinvoice, checkoutpage, requestpayment, paymentredirect, webhook

urlpatterns = [

    url(r'^viewinvoice/$', viewinvoice.as_view()),
    url(r'^checkoutpage/$', checkoutpage, name='checkoutpage'),
    url(r'^requestpayment/$', requestpayment, name='requestpayment'),
    url(r'^paymentredirect/$', paymentredirect, name='paymentredirect'),
    url(r'^webhook/$', webhook, name='webhook'),


]
