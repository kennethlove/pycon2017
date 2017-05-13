from django.contrib import admin
from image_cropping import ImageCroppingMixin

from . import models


class ImageInline(ImageCroppingMixin, admin.StackedInline):
    model = models.Image


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
    inlines = [ImageInline]
    prepopulated_fields = {'slug': ('name',)}
    radio_fields = {'featured': admin.HORIZONTAL}


@admin.register(models.Image)
class ImageAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

admin.site.register(models.Category)
