from django.http import HttpResponseRedirect

from .serializers import *
from rest_framework import generics

from rest_framework.response import Response

# Create your views here.


import string
import random

# how to create random string
"""
initializing size of string
N = 7

using random.choices()
generating random strings
res = ''.join(random.choices(string.ascii_uppercase +string.digits, k=N))

print result
"""



class StoreUrlView(generics.CreateAPIView):
    queryset = StoreUrl.objects.all()
    serializer_class = StoreUrlSerializers

    def post(self, request, *args, **kwargs):
        payload = request.data
        payload['shorturl'] = "http://127.0.0.1:8000/storeurl/" + ''.join(random.choices(string.ascii_letters +string.digits, k=5))
        print(payload, '===========')
        serializer = self.get_serializer(data=payload)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)


class UrlRedirectView(generics.ListAPIView):
    queryset = StoreUrl.objects.all()
    serializer_class = StoreUrlSerializers

    def get(self, request, *args, **kwargs):
        url = "http://127.0.0.1:8000/storeurl/" + kwargs['url']
        redirect_link_url = StoreUrl.objects.get(shorturl=url)
        if redirect_link_url:
            return HttpResponseRedirect(redirect_to=redirect_link_url.longurl)
        else:
            return Response('invalid url', status=200)