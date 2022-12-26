import string
import random

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator
from .models import *
from django.utils import timezone


class StoreUrlSerializers(serializers.ModelSerializer):
    longurl = serializers.URLField()
    shorturl = serializers.CharField()

    class Meta:
        model = StoreUrl
        fields = ['id', 'longurl', 'shorturl']

    def validate_shorturl(self, value):
        obj = StoreUrl.objects.filter(shorturl=value)
        if obj:
            value = "http://127.0.0.1:8000/storeurl/" + ''.join(
                random.choices(string.ascii_letters + string.digits + string.ascii_uppercase, k=7))
            self.validate_shorturl(value)
        return value
