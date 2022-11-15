from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from Hotel.decorators import *
from django.contrib import messages
from Hotel.models import *


@signin_required
@guest_login
def guest_home(request):
    hotel_view = Hotel.objects.all()
    return render(request,"dashboard.html",{"hot": hotel_view})

@signin_required
@guest_login
def view_room(request,id):
    hotel_name = Hotel.objects.get(id=id)
    rooms= Room.objects.filter(hotel=hotel_name,availability="Open")
    return render(request, "view-room.html", {"rooms": rooms})


@signin_required
def logout_view(request):
    logout(request)
    return redirect("signin")