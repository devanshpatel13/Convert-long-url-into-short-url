import logging

from django.test import TestCase

# Create your tests here.

import os, sys
import django

sys.path.append('/home/plutusdev/Projects/Task/shorturl')
os.environ['DJANGO_SETTINGS_MODULE'] = 'shorturl.settings'
print(os.environ['DJANGO_SETTINGS_MODULE'])
os.environ['SECRET_KEY'] = 'django-insecure-06929wb#(0pold7-q4v%y#9z@ab&2y0)wsjh(bj7in@jp$a75&'
from datetime import datetime

django.setup()
from app.models import StoreUrl
# import pdb;pdb.set_trace()
queryset = StoreUrl.objects.all()
# import pdb;
print(os.getenv("DATABASE_NAME"))
print("Inside crontab 1", queryset)
# pdb.set_trace()
for created_date in queryset:
    print("inside crontab 2")
    if (datetime.now() - created_date.created_date).days == 0:
        print("insdie crontab 3")
        created_date.delete()
        print("Yeh Bro........, condition is checked....")


