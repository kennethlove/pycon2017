from django.contrib import admin
from django.db.models import Count, Sum
from django.utils import timezone

from . import forms
from . import models


class PurchaseItemInline(admin.TabularInline):
    model = models.PurchaseItem


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
    save_as = True
    save_on_top = True
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
    inlines = [PurchaseItemInline]
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


@admin.register(models.PurchaseSummary)
class PurchaseSummaryAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context)
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        metrics = {
            'total': Sum('quantity'),
            'total_sales': Sum('product__price'),
        }
        response.context_data['summary'] = list(
            qs.values('product__name').annotate(**metrics).order_by('-quantity')
        )
        response.context_data['summary_total'] = dict(
            qs.aggregate(**metrics)
        )
        return response

admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.PurchaseItem)
