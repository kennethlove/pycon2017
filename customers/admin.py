from django.contrib import admin
from django.db.models import Count

from . import models


class BigOrderFilter(admin.SimpleListFilter):
    title = 'big order'
    parameter_name = 'big_order'

    def lookups(self, request, model_admin):
        return (
            ('1', 'True'),
            ('0', 'False'),
        )

    def queryset(self, request, queryset):
        if self.value() == '1':
            return queryset.annotate(Count('items')).filter(items__count__gte=2)
        return queryset


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['admin_name']


@admin.register(models.Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['customer', 'placed_at', 'shipped_at', 'shipped', 'total']
    list_editable = ['shipped']
    list_filter = ['shipped', 'placed_at', 'shipped_at', BigOrderFilter]
    ordering = ['placed_at']

admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.PurchaseItem)
