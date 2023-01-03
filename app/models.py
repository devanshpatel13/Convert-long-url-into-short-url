from django.db import models
import datetime

# Create your models here.


class StoreUrl(models.Model):
    longurl = models.URLField(unique=False)
    shorturl = models.URLField(unique=True, max_length=120, db_index=True)
    created_date = models.DateTimeField()


        
