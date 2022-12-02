from django.db import models

# Create your models here.


class StoreUrl(models.Model):
    longurl = models.URLField()
    shorturl = models.URLField()
