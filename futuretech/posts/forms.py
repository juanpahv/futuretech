from django import forms
from .models import Post, PostImage

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['title', 'description', 'condition', 'categoryId', 'originalPrice', 'brandId', 'stock']
    labels = {
      'title': 'Title',
      'description': 'Description',
      'condition': 'Condition',
      'categoryId': 'Category',
      'originalPrice': 'Original Price',
      'brandId': 'Brand',
      'stock': 'Stock',
    }
    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-control'}),
      'description': forms.TextInput(attrs={'class': 'form-control'}),
      'condition': forms.Select(attrs={'class': 'form-control'}),
      'categoryId': forms.Select(attrs={'class': 'form-control'}),
      'originalPrice': forms.NumberInput(attrs={'class': 'form-control'}),
      'brandId': forms.Select(attrs={'class': 'form-control'}),
      'stock': forms.NumberInput(attrs={'class': 'form-control'}),
    }

class PostImageForm(forms.ModelForm):
  class Meta:
    model = PostImage
    fields = ['image', 'postId']
    