from django import forms
from django.contrib.auth.models import User
from Hotel.models import *
from django.contrib.auth.forms import UserCreationForm

class SignInForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput( attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))

class HotelRegistration(forms.ModelForm):
    username= forms.CharField(label=" ",label_suffix=" ",widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}))
    password1 = forms.CharField(label=" ", label_suffix=" ",widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}))
    password2 = forms.CharField(label=" ", label_suffix=" ", widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Confirm password"}))
    class Meta:
        model=Hotel
        fields="__all__"

class GuestRegistration(forms.ModelForm):
    username = forms.CharField(label=" ", label_suffix=" ", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}))
    password1 = forms.CharField(label=" ", label_suffix=" ",widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}))
    password2 = forms.CharField(label=" ", label_suffix=" ", widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Confirm password"}))
    class Meta:
        model=BaseUser
        fields="__all__"
