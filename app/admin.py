from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(StoreUrl)
class StoreUrlAdmin(admin.ModelAdmin):
    list_display = ['id', 'longurl', 'shorturl']