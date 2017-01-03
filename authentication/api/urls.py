from django.conf.urls import include, url
from django.contrib import admin
from .views import HomepageAPIView

urlpatterns = [

    url(r'^$', HomepageAPIView.as_view(), name='homepage'),
]
