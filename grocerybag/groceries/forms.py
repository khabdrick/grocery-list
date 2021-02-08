from django import forms
from django.forms import widgets

from .models import Grocery


class GroceryForm(forms.ModelForm):
    class Meta:
        fields = ["item_name", "item_quantity", "item_status"]
        model = Grocery
        widgets={
            'item_name': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Item name'}
            ),
            'item_quantity': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Item quantity'}
            ),
            'item_status': forms.Select(
                attrs={'class':'form-control',}
            )
        }
            

        
class GroceryUpdateForm(forms.ModelForm):
    class Meta:
        fields = ["item_name", "item_quantity", "item_status"]
        model = Grocery
        widgets={
            'item_name': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Item name'}
            ),
            'item_quantity': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Item quantity'}
            ),
            'item_status': forms.Select(
                attrs={'class':'form-control',}
            )
        }
  
