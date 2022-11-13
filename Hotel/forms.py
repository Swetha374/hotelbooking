from django import forms
from Admin.models import *
# from django.contrib.auth.models import User
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


                ]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}),
            "password": forms.PasswordInput(attrs={"class": "form-control","placeholder": "password1"}),

        }


class Registration(forms.ModelForm):

    class Meta:
        model=User
        fields=[
            "name",
            "dob",
            "gender",
            "mobile",
            "email",
            "usertype",
            "username",
            "password"

        ]

    widgets = {
        "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}),
        "password": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "password1"}),

    }

class AddRoomForm(forms.ModelForm):
    class Meta:
        model=Room
        fields="__all__"


class EditRoomForm(forms.ModelForm):
    class Meta:
        model=Room
        exclude=("hotel",)