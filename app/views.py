import logging

from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from rest_framework.exceptions import ValidationError

from .serializers import *
from rest_framework import generics
from django.db import DatabaseError
from rest_framework.response import Response
import datetime
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
        payload['shorturl'] = "http://127.0.0.1:8000/storeurl/" + ''.join(
            random.choices(string.ascii_letters + string.digits + string.ascii_uppercase, k=7))
        payload['created_date'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            serializer = self.get_serializer(data=payload, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=201)
        except DatabaseError as db_error:
            import pdb; pdb.set_trace()
            raise ValidationError({'message': 'Something went to wrong '}) from db_error
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
