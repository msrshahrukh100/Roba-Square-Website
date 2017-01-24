from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'tijarah.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #nested admin url
    url(r'^nested_admin/', include('nested_admin.urls')),
    #django all auth urls
    url(r'^accounts/', include('allauth.urls')),
    # for the notfications 
    url('^inbox/notifications/', include('notifications.urls', namespace='notifications')),

    #local apps url
    url(r'^', include('authentication.urls',namespace='authentication')),
    url(r'^api/authentication/', include('authentication.api.urls',namespace='authentication-api')),
    url(r'^cart/', include('cart.urls',namespace='cart')),
    url(r'^shop/', include('shopping.urls',namespace='shopping')),
    url(r'^review/', include('productreviews.urls',namespace='review')),
    url(r'^social/', include('social.urls',namespace='social')),
    url(r'^blog/', include("blog.urls", namespace='blog')),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
