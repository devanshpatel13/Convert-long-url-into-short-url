from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [

    path("storeurl", StoreUrlView.as_view(), name="storeurl"),
    path("storeurl/<str:url>", UrlRedirectView.as_view(), name="redirect url"),
    path('auth', include('rest_framework.urls', namespace='rest_framework'))
]
