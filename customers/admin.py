from django.contrib import admin

from . import models

admin.site.register(models.Customer)
admin.site.register(models.Purchase)
admin.site.register(models.PurchaseItem)
