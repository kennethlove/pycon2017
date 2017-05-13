from django.contrib import admin
from django.db.models import Count
from django.utils import timezone

from . import forms
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
    form = forms.CustomerForm
    list_display = ['admin_name']
    search_fields = ['name']


def ship(modeladmin, request, queryset):
    queryset.update(
        shipped=True,
        shipped_at=timezone.now()
    )
ship.short_description = 'Mark purchases as shipped now'


@admin.register(models.Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    actions = [ship]
    date_hierarchy = 'placed_at'
    list_display = ['customer', 'placed_at', 'shipped_at', 'shipped', 'total']
    list_editable = ['shipped']
    list_filter = ['shipped', 'placed_at', 'shipped_at', BigOrderFilter]
    ordering = ['placed_at']
    search_fields = ['customer__name', 'items__name']

    fieldsets = (
        (None, {
            'fields': (
                ('customer', 'total', 'shipped'),
                'discount_code'
            )
        }),
        ('Dates', {
            'classes': ('collapse',),
            'fields': ('placed_at', 'shipped_at'),
        })
    )

admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.PurchaseItem)
