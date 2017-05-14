from django.contrib import admin
from django.db import models as dj_models
from image_cropping import ImageCroppingMixin

from . import models
from . import widgets


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
    formfield_overrides = {
        dj_models.TextField: {'widget': widgets.WYSIWYGTextarea}
    }
    inlines = [ImageInline]
    prepopulated_fields = {'slug': ('name',)}
    radio_fields = {'featured': admin.HORIZONTAL}

    class Media:
        css = {
            'all': ('trumbo/ui/trumbowyg.min.css',)
        }
        js = (
            'https://code.jquery.com/jquery-3.2.1.min.js',
        )


@admin.register(models.Image)
class ImageAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

admin.site.register(models.Category)
