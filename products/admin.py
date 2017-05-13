from django.contrib import admin

from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    fields = (
        ('name', 'slug'),
        'description',
        ('price', 'quantity'),
        'featured',
        ('serial_number', 'location'),
        'categories'
    )
    filter_horizontal = ['categories']
    prepopulated_fields = {'slug': ('name',)}
    radio_fields = {'featured': admin.HORIZONTAL}

admin.site.register(models.Image)
admin.site.register(models.Category)
