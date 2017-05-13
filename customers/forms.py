from django import forms

from . import models


class CustomerForm(forms.ModelForm):
    class Meta:
        fields = ('email', 'name', 'street_1', 'street_2',
                  'city', 'state', 'country', 'postal_code')
        model = models.Customer
