from django.db import models

# Create your models here.


class StoreUrl(models.Model):
    longurl = models.URLField(unique=False)
    shorturl = models.URLField(unique=True, max_length=120, db_index=True)
