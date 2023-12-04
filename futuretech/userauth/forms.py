from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['username', 'password', 'email', 'first_name', 'last_name']
    widgets = {
      'username': forms.TextInput(attrs={'class': 'form-control'}),
      'password': forms.PasswordInput(),
    }
    
