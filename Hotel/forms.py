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
        exclude = ("hotel","total_price")

class EditRoomForm(forms.ModelForm):
    class Meta:
        model=Room
        exclude=("hotel",)

class GuestEditRoomForm(forms.ModelForm):
    class Meta:
        model=Room
        exclude=("availability","hotel","price_of_adult","price_of_child","room_name")


class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields = "__all__"
        exclude=("guest_name","guest_mobile","status","guest","room","no_of_days","total","total_bookingss")

        widgets={
           "stay_start_date":forms.DateInput(attrs={"class":"form-control","type":"date"}),
            "stay_end_date": forms.DateInput(attrs={"class": "form-control", "type": "date"})
        }

class OwnerBookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields="__all__"
        exclude=("guest","status","room","no_of_days","total","total_bookingss")

        widgets = {
            "stay_start_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "stay_end_date": forms.DateInput(attrs={"class": "form-control", "type": "date"})
        }


class OwnerEditBookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields = "__all__"
        exclude=("room","guest","guest_name","total_bookingss","guest_mobile","no_of_days","total","occupancy_adult","occupancy_child")

        widgets = {
            "stay_start_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "stay_end_date": forms.DateInput(attrs={"class": "form-control", "type": "date"})
        }
class GuestEditBookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields = "__all__"
        exclude=("room","guest","total_bookingss","guest_name","guest_mobile","status","price_of_adult","price_of_child","total","no_of_days")

        widgets = {
            "stay_start_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "stay_end_date": forms.DateInput(attrs={"class": "form-control", "type": "date"})
        }

class EditAcceptedForm(forms.ModelForm):
    class Meta:
        model=PerDayBooking
        fields="__all__"
        exclude =("bookingss","date")