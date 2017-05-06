import random

import factory
from factory.django import DjangoModelFactory
from django.utils.text import slugify
from faker import Faker

from . import models

fake = Faker()


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = models.Product

    slug = factory.LazyAttribute(lambda o: slugify(o.name))
    description = factory.Faker('sentence')
    price = factory.Faker('pydecimal', left_digits=3, right_digits=2, positive=True)
    location = factory.Faker('isbn10', separator='')
    serial_number = factory.Faker('uuid4')
    quantity = factory.Faker('random_number', digits=4)

    @factory.lazy_attribute
    def name(self):
        return ' '.join(fake.words(nb=3)).title()

    @factory.post_generation
    def categories(self, create, extracted, **kwargs):
        categories = models.Category.objects.all()
        for category in random.choices(categories, k=random.randint(1, len(categories))):
            self.categories.add(category)
