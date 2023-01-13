from django.urls import path
from .views import *

urlpatterns = [

    path("store-url", StoreUrlView.as_view(), name="store_url"),
    path("<str:url>", UrlRedirectView.as_view(), name="redirect_url"),
]
