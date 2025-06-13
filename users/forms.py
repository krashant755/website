from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'city', 'state', 'zip_code', 'country', 'phone']
        widgets = {
            'address': forms.TextInput(attrs={'placeholder': 'Enter your address'}),
            'city': forms.TextInput(attrs={'placeholder': 'Enter your city'}),
            'state': forms.TextInput(attrs={'placeholder': 'Enter your state/province'}),
            'zip_code': forms.TextInput(attrs={'placeholder': 'Enter your ZIP code'}),
            'country': forms.TextInput(attrs={'placeholder': 'Enter your country'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter your phone number'}),
        } 