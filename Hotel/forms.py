from django import forms
from django.contrib.auth.models import User
from Hotel.models import *
from django.contrib.auth.forms import UserCreationForm

class SignInForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput( attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))


class HotelRegistration(forms.ModelForm):
    class Meta:
        model=Hotel
        fields=["hotel_name",
                "image",
                "address",
                "location",
                "star_rating",
                "owner_name",
                "owner_image",
                "owner_email",
                "owner_mobile",
                "is_admin",
                "is_hotel",
                "is_guest",
                "username",
                "password1",
                "password2"
                ]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control","placeholder": "password1"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control","placeholder": "password2"}),
        }

class GuestRegistration(forms.ModelForm):

    class Meta:
        model=User
        fields=[
            "name",
            "dob",
            "gender",
            "mobile",
            "email",
            "is_admin",
            "is_hotel",
            "is_guest",
            "username",
            "password1",
            "password2",

        ]

    widgets = {
        "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}),
        "password1": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "password1"}),
        "password2": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "password2"}),
    }