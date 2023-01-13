from django.db import models


class StoreUrl(models.Model):
    longurl = models.URLField(unique=False)
    shorturl = models.URLField(unique=True, max_length=120, db_index=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.shorturl}"
