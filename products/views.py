from django.views import generic

from . import models


class AllProducts(generic.ListView):
    model = models.Product
