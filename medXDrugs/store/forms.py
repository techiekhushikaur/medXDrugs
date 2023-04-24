from django.forms import ModelForm
from django import forms
from .models import *

class ShippingForm(ModelForm):
    class Meta:
        model = ShippingAddress
        fields = '__all__'
        exclude = ['user']


class ShippingUpdateForm(ModelForm):
    class Meta:
        model = ShippingAddress
        fields = '__all__'
        exclude = ['user']

class AddCategory(ModelForm):
    class Meta:
        model= ProductCategories
        fields = '__all__'
        exclude=['ngo_true']

class AddItems(ModelForm):
    class Meta:
        model= Product
        fields = '__all__'
        exclude=['category','ngo_true']

class EditItems(ModelForm):
    
    class Meta:
        model= Product
        fields = ['image']
    image = forms.ImageField(label=False,required=False)

class EditCategory(ModelForm):
     class Meta:
        model= ProductCategories
        fields = ['image']
     image = forms.ImageField(label=False,required=False)
