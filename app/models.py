from django.db import models

# Create your models here.


class StoreUrl(models.Model):
    longurl = models.URLField(unique=True)
    shorturl = models.CharField(unique=True, max_length=120)
