from django import forms
from .models import CartItem

class CartItemForm(forms.ModelForm):
  class Meta:
    model = CartItem
    fields = ['userId','postId', 'quantity']
    widgets = {
      'userId': forms.HiddenInput(),
      'postId': forms.HiddenInput(),
      'quantity': forms.NumberInput(attrs={'class': 'form-form-control form-control-sm text-right', 'min': 1, 'max': 100, 'value': 1}),
    }