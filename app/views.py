import logging

from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from rest_framework.exceptions import ValidationError

from .serializers import *
from rest_framework import generics
from django.db import DatabaseError
from rest_framework.response import Response

# Create your views here.
logger = logging.getLogger(__name__)

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


class StoreUrlView(generics.ListCreateAPIView):
    queryset = StoreUrl.objects.all()
    serializer_class = StoreUrlSerializers

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)

    def post(self, request, *args, **kwargs):
        payload = request.data
        # payload['shorturl'] = "http://127.0.0.1:8000/storeurl/testing"

        # payload['shorturl'] = "http://127.0.0.1:8000/storeurl/" + ''.join(
        #     random.choices(string.ascii_letters + string.digits + string.ascii_uppercase, k=5))
        # payload['shorturl'] = ''.join(random.choices(string.ascii_letters + string.digits + string.ascii_uppercase, k=5))
        payload['shorturl'] = "XlPdG12321733"
        # payload['longurl'] = "http://127.0.0.1:8000/storeurl/" + ''.join(
        #     random.choices(string.ascii_letters + string.digits + string.ascii_uppercase, k=70))
        # obj = StoreUrl.objects.filter(shorturl=payload['shorturl'])
        #
        # if obj:
        #     payload['shorturl'] = "http://127.0.0.1:8000/storeurl/aa"

        # payload['shorturl'] = "http://127.0.0.1:8000/storeurl/" + ''.join(
        #     random.choices(string.ascii_letters + string.digits + string.ascii_uppercase, k=5))

        # import pdb; pdb.set_trace()
        # for i in range(100000000):
        #     new = payload['shorturl']
        #     new1 = payload['longurl']
        #     new += str(i)
        #     new1 += str(i)
        #     pay = {'shorturl': new, 'longurl': new1}
        try:
            serializer = self.get_serializer(data=payload, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=201)
        except DatabaseError as db_error:
            raise ValidationError({'message': 'Duplicate Long URL.'}) from db_error
        except Exception as e:
            raise e

class UrlRedirectView(generics.ListAPIView):
    queryset = StoreUrl.objects.all()
    serializer_class = StoreUrlSerializers

    def get(self, request, *args, **kwargs):
        url = "http://127.0.0.1:8000/storeurl/" + kwargs['url']
        redirect_link_url = StoreUrl.objects.get(shorturl=url)
        if redirect_link_url:
            # return HttpResponseRedirect(redirect_to=redirect_link_url.longurl)
            return redirect(redirect_link_url.longurl)
        else:
            return Response('invalid url', status=200)
