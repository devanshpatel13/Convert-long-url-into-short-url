import string
import random

from rest_framework import serializers
from .models import *


class StoreUrlSerializers(serializers.ModelSerializer):
    longurl = serializers.URLField()
    shorturl = serializers.CharField()
    created_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M")

    class Meta:
        model = StoreUrl
        fields = ['id', 'longurl', 'shorturl', 'created_date']

    def validate_shorturl(self, value):
        """

        @param value:
        @return:
        """
        if StoreUrl.objects.filter(shorturl=value):
            value = "http://127.0.0.1:8000/storeurl/" + ''.join(
                random.choices(string.ascii_letters + string.digits + string.ascii_uppercase, k=7))
            self.validate_shorturl(value)
        return value
