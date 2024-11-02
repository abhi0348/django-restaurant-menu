from django import forms
from .models import dish,Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MenuForm(forms.ModelForm):
    class Meta:
        model = dish
        fields = ['name', 'price', 'description', 'category']
        
# Form for user signup
class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']