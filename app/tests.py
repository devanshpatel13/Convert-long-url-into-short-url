import logging

from django.test import TestCase

# Create your tests here.

import os, sys
import django

sys.path.append('/home/plutusdev/Projects/Task/shorturl')
os.environ['DJANGO_SETTINGS_MODULE'] = 'shorturl.settings'
os.environ['SECRET_KEY'] = 'django-insecure-_b^bu(!$ka*ggw=$68!6g#(2%xt-)klie9!8uu&ze63b9539-0'
from datetime import datetime

django.setup()
from app.models import StoreUrl

queryset = StoreUrl.objects.all()

for created_date in queryset:
    if (datetime.now() - created_date.created_date).days == 0:
        created_date.delete()
        print("Yeh Bro........, condition is checked....")



print(created_date)