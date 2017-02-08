from django.conf.urls import include, url
from .views import checkoutpage, requestpayment, paymentredirect, webhook, generateinvoice, myorders, returns

urlpatterns = [
	url(r'^generateinvoice/$', generateinvoice, name='generateinvoice'),
    url(r'^checkoutpage/$', checkoutpage, name='checkoutpage'),
    url(r'^requestpayment/$', requestpayment, name='requestpayment'),
    url(r'^paymentredirect/$', paymentredirect, name='paymentredirect'),
    url(r'^webhook/$', webhook, name='webhook'),
    url(r'^myorders/$', myorders, name='myorders'),
    url(r'^returns/(?P<id>\d+)$', returns, name='returns'),


]
