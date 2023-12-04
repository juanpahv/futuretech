from django import forms
from .models import Post

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['title', 'description', 'condition', 'categoryId', 'originalPrice', 'brandId', 'stock', 'discountPercentage']
    labels = {
      'title': 'Title',
      'description': 'Description',
      'condition': 'Condition',
      'categoryId': 'Category',
      'originalPrice': 'Original Price',
      'brandId': 'Brand',
      'stock': 'Stock',
      'discountPercentage': 'Discount Percentage',
    }
    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-control'}),
      'description': forms.TextInput(attrs={'class': 'form-control'}),
      'condition': forms.Select(attrs={'class': 'form-control'}),
      'categoryId': forms.Select(attrs={'class': 'form-control'}),
      'originalPrice': forms.NumberInput(attrs={'class': 'form-control'}),
      'brandId': forms.Select(attrs={'class': 'form-control'}),
      'stock': forms.NumberInput(attrs={'class': 'form-control'}),
      'discountPercentage': forms.NumberInput(attrs={'class': 'form-control'}),
    }