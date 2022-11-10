from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from Hotel.decorators import signin_required


@signin_required
def guest_home(request):
    return render(request,"dashboard.html")

@signin_required
def logout_view(request):
    logout(request)
    return redirect("signin")