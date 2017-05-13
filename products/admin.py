from django.contrib import admin
from image_cropping import ImageCroppingMixin

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


@admin.register(models.Image)
class ImageAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

admin.site.register(models.Category)
