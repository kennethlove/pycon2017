from django.contrib import admin

from . import models

class CustomerAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.Purchase)
admin.site.register(models.PurchaseItem)
