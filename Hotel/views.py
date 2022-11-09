from django.shortcuts import render, redirect

# Create your views here.
from Hotel import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from Hotel.models import *


def login_view(request):
    if request.method == "GET":
        form = forms.SignInForm()
        return render(request, "signin.html", {"form": form})

    if request.method == "POST":
        form = forms.SignInForm(request.POST, files=request.FILES)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                if request.user.is_superuser:
                    return render(request, "index.html")

                if request.user.is_staff:
                    return render(request, "dashboard.html")
                else:
                    return render(request, "home.html")
        else:
            messages.error(request, "invalid credentials")
            return render(request, "signin.html", {"form": form})
    return render(request, "signin.html")

def hotel_registration(request):
    if request.method == "GET":
        form=forms.HotelRegistration()
        return render(request,"hotel-reg.html",{"form":form})
    if request.method == "POST":
        form=forms.HotelRegistration(request.POST, files=request.FILES)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            messages.success(request,"your account has been created")
            return render(request, "signin.html", {"form": form})
    else:
        messages.error(request,"registration failed")
    return render(request,"hotel-reg.html",{"form":form})

def guest_registration(request):
    if request.method == "GET":
        form=forms.GuestRegistration()
        return render(request,"guest-reg.html",{"form":form})
    if request.method == "POST":
        form=forms.GuestRegistration(request.POST, files=request.FILES)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            messages.success(request,"your account has been created")
            return render(request, "signin.html", {"form": form})
    else:
        messages.error(request,"registration failed")
    return render(request,"guest-reg.html",{"form":form})

