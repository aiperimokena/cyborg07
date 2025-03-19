from django import forms
from .models import Product

class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'category',
            'title',
            'main_image',
            'images',
            'description',
            'price',
            'quantity'
        )

class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'category',
            'title',
            'main_image',
            'images',
            'description',
            'price',
            'quantity'
        )

