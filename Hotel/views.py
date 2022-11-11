from django.shortcuts import render, redirect

# Create your views here.
from Hotel import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from Hotel.models import *
from Hotel.decorators import signin_required



def login_view(request):
    if request.method == "GET":
        form = forms.SignInForm()
        return render(request, "signin.html", {"form": form})

    if request.method == "POST":
        form = forms.SignInForm(request.POST, files=request.FILES)
        if form.is_valid():

            uname = form.cleaned_data.get("username")
            pwd = form.cleaned_data.get("password")
            user = authenticate(request, username=uname, password=pwd)
            print(user)
            if user:
                login(request, user)
                if request.user.is_superuser:  # user type
                    return redirect("admin-home")
                if request.user.usertype == 'Hotel':
                    return redirect("hotel-home")
                if request.user.usertype == 'Guest':
                    return render(request, "dashboard.html")
        else:
            messages.error(request, "invalid username or password")
        messages.error(request,"please login")
        return render(request, "signin.html", {"form": form})

def hotel_registration(request):
    if request.method == "GET":
        form=forms.HotelRegistration()
        return render(request, "hotel-reg.html", {"form": form})
    if request.method == "POST":
        form=forms.HotelRegistration(request.POST, files=request.FILES)
        if form.is_valid():
            form.instance.owner=request.user
            form.save()
            messages.success(request,"your hotel has been added")
            return redirect("list-hotel")
    else:
        messages.error(request, "registration failed")
    return render(request, "hotel-reg.html", {"form": form})


def registration(request):
    if request.method == "GET":
        form=forms.Registration()
        return render(request, "guest-reg.html", {"form": form})

    if request.method == "POST":
        form=forms.Registration(request.POST, files=request.FILES)
        if form.is_valid():
            user=User.objects.create_user(**form.cleaned_data)
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            messages.success(request,"your account has been created")

    else:
        messages.error(request, "registration failed")
    return render(request,"guest-reg.html",{"form":form})



@signin_required
def hotel_home(request):
    return render(request,"home.html")

def list_hotel(request):
    return render(request,"list-hotel.html")