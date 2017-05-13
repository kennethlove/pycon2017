from django.contrib import admin

from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'description']

admin.site.register(models.Image)
admin.site.register(models.Category)
