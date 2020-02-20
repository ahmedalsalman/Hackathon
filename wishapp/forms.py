from django import forms
from .models import Wish
from django.contrib.auth.models import User


class WishForm(forms.ModelForm):
    class Meta:
        model = Wish
        exclude = ['user']


#class ItemForm(forms.ModelForm):
#    class Meta:
#        model = Item
#        exclude = ['restaurant',]


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

        widgets={
        'password': forms.PasswordInput(),
        }


class SigninForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())
