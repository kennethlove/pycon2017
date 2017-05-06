import datetime
import random

from django.utils import timezone

import factory
from factory.django import DjangoModelFactory
from faker import Faker

from . import models
from products.factories import ProductFactory
from products.models import Product

fake = Faker()
products = Product.objects.all()


class CustomerFactory(DjangoModelFactory):
    class Meta:
        model = models.Customer

    name = factory.Faker('name')
    email = factory.Faker('email')
    street_1 = factory.Faker('street_address')
    city = factory.Faker('city')
    state = factory.Faker('state_abbr')
    country = factory.Faker('country_code')
    postal_code = factory.Faker('postalcode')

    @factory.lazy_attribute
    def street_2(self):
        if random.choice((0, 0, 0, 1, 1)):
            return fake.secondary_address()
        return ''


class PurchaseFactory(DjangoModelFactory):
    class Meta:
        model = models.Purchase

    customer = factory.SubFactory(CustomerFactory)
    placed_at = factory.Faker('date_time_this_year')
    total = factory.Faker('pydecimal', left_digits=4, right_digits=2, positive=True)
    shipped = factory.LazyAttribute(lambda o: bool(o.shipped_at))

    @factory.lazy_attribute
    def shipped_at(self):
        if random.choice([0]*7 + [1]):
            return fake.date_time_between_dates(
                self.placed_at,
                timezone.now()
            )
        return None

    @factory.lazy_attribute
    def discount_code(self):
        if random.choice((0, 1)):
            return fake.word()
        return ''


class PurchaseItemFactory(DjangoModelFactory):
    class Meta:
        model = models.PurchaseItem

    product = factory.SubFactory(ProductFactory)
    purchase = factory.SubFactory(PurchaseFactory)
    quantity = factory.Faker('random_number', digits=2)
