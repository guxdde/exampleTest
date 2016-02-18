# -*- coding: utf-8 -*-

from django import forms
from .models import Product


class ProductAdminForm(forms.ModelForm):
    """docstring for ProductAdminForm"""
    class Meta:
        model = Product
        exclude = []

    def clean_price(self):
        if self.cleaned_data['price'] <= 0:
            raise forms.ValidationError("价格必须大于０")
        return self.cleaned_data['price']
