
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import *
from django.utils import timezone


class StoreUrlSerializers(serializers.ModelSerializer):
    class Meta:
        model = StoreUrl
        fields = "__all__"