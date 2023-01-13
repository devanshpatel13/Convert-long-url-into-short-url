import logging

from django.shortcuts import redirect
from rest_framework.exceptions import ValidationError

from .serializers import *
from rest_framework import generics, status
from django.db import DatabaseError
from rest_framework.response import Response
import datetime

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

    def post(self, request, *args, **kwargs):
        payload = request.data
        payload['shorturl'] = "http://127.0.0.1:8000/" + ''.join(
            random.choices(string.ascii_letters + string.digits + string.ascii_uppercase, k=7))
        payload['created_date'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            serializer = self.get_serializer(data=payload, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except DatabaseError as db_error:
            raise ValidationError({'message': 'Something went to wrong '}) from db_error
        except Exception as e:
            raise e


class UrlRedirectView(generics.ListAPIView):
    queryset = StoreUrl.objects.all()
    serializer_class = StoreUrlSerializers

    def get(self, request, *args, **kwargs):
        url = "http://127.0.0.1:8000/" + kwargs['url']
        redirect_link_url = StoreUrl.objects.get(shorturl=url)
        if redirect_link_url:
            return redirect(redirect_link_url.longurl)
        else:
            return Response('invalid url', status=status.HTTP_404_NOT_FOUND)
