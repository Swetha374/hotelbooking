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
            if user is not None and user.is_admin:
                login(request, user)
                return redirect("admin-home")
            # elif user is not None and Hotel.is_hotel:
            #     login(request, user)
            #     return redirect("hotel-home")

            elif user is not None and user.is_guest:
                login(request, user)
                return redirect("guest-home")

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
            Hotel.objects.create(**form.cleaned_data)
            form.save()
            messages.success(request,"your account has been created")
            return redirect("signin")
    else:
        messages.error(request, "registration failed")
    return render(request, "guest-reg.html", {"form": form})


def guest_registration(request):
    if request.method == "GET":
        form=forms.GuestRegistration()
        return render(request, "guest-reg.html", {"form": form})

    if request.method == "POST":
        form=forms.GuestRegistration(request.POST, files=request.FILES)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            messages.success(request,"your account has been created")
            return redirect("signin")
    else:
        messages.error(request, "registration failed")
    return render(request,"guest-reg.html",{"form":form})

@signin_required
def hotel_home(request):
    return render(request,"home.html")

