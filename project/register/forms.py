from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Orders


class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'

        labels = {
            'oid': 'Order ID',
            'fname' : 'First Name',
            'lname' : 'Last Name.' ,
            'price' : 'Price' ,
            'mail' : 'Email ID',
            'addr' : 'Address' ,
        }

        widgets  ={
            'oid' : forms.NumberInput(attrs={'placeholder': 'enter a number'}),
            'fname' : forms.TextInput(attrs={'placeholder': 'your name here'}),
            'lname' : forms.TextInput(attrs={'placeholder': 'your last name here'}),
            'price' : forms.NumberInput(attrs={'placeholder': 'only numbers'}),
            'mail' : forms.EmailInput(attrs={'placeholder': 'eg. your-email@gmail.com'}),
            'addr' : forms.Textarea(attrs={'placeholder': 'your adress here'}),
        }

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')