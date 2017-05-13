from django.contrib import admin

from . import models

class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['customer', 'placed_at', 'shipped_at', 'shipped', 'total']
    ordering = ['placed_at']

admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.PurchaseItem)
