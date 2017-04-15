from django.shortcuts import get_object_or_404
from django.views import generic

from . import models


class AllProducts(generic.ListView):
    model = models.Product


class ByCategory(generic.ListView):
    template_name = 'products/product_list.html'

    def get_queryset(self):
        category = get_object_or_404(models.Category, name__iexact=self.kwargs.get('category'))
        return category.product_set.all()


class Detail(generic.DetailView):
    model = models.Product
