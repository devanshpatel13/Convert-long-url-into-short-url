from django.contrib import admin
from .models import StoreUrl


@admin.register(StoreUrl)
class StoreUrlAdmin(admin.ModelAdmin):
    list_display = ['id', 'longurl', 'shorturl', 'created_date']
