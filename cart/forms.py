from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'state', 'zip_code', 'country', 'order_note']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter your phone number'}),
            'address': forms.TextInput(attrs={'placeholder': 'Enter your address'}),
            'city': forms.TextInput(attrs={'placeholder': 'Enter your city'}),
            'state': forms.TextInput(attrs={'placeholder': 'Enter your state/province'}),
            'zip_code': forms.TextInput(attrs={'placeholder': 'Enter your ZIP code'}),
            'country': forms.TextInput(attrs={'placeholder': 'Enter your country'}),
            'order_note': forms.Textarea(attrs={'placeholder': 'Any special notes for your order?', 'rows': 3}),
        } 