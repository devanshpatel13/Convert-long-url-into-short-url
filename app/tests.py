import logging

from django.test import TestCase

# Create your tests here.

import os, sys
import django

sys.path.append('/home/plutusdev/Projects/Task/shorturl')
os.environ['DJANGO_SETTINGS_MODULE'] = 'shorturl.settings'
print(os.environ['DJANGO_SETTINGS_MODULE'])
os.environ['SECRET_KEY'] = os.getenv('SECRET_KEYS')
from datetime import datetime

django.setup()
from app.models import StoreUrl

queryset = StoreUrl.objects.all()
print(os.getenv("DATABASE_NAME"))
for created_date in queryset:
    if (datetime.now() - created_date.created_date).days == 0:
        created_date.delete()
