from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=["name", "sku", "price", "stock_quantity"]
        widgets={
            'name':forms.TextInput(attrs={
                'class':'form_input',
                'placeholder':'e.g. Samsung Monitor'
            }),
            'sku': forms.TextInput(attrs={
                'class': 'form_input', 
                'placeholder': 'e.g. SM-4001'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form_input', 
                'placeholder': 'e.g. 199.99'
            }),
            'stock_quantity': forms.NumberInput(attrs={
                'class': 'form_input', 
                'placeholder': 'Available stock'
            }),
        }

