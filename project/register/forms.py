from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Orders, Profile

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

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='')
    image = forms.ImageField(required=False, help_text='')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'image')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            if self.cleaned_data['image']:
                Profile.objects.create(user=user, image=self.cleaned_data['image'])
            else:
                Profile.objects.create(user=user)
        return user
    

class LoginForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']