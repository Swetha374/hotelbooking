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
            form.instance.owner_name=request.user
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
            return redirect("signin")

    else:
        messages.error(request, "registration failed")
    return render(request,"guest-reg.html",{"form":form})



@signin_required
def hotel_home(request):
    return render(request,"home.html")
@signin_required
def list_hotel(request):
   hotel_list=Hotel.objects.filter(owner_name=request.user)
   return render(request,"list-hotel.html",{"hotel":hotel_list})

@signin_required
def hotel_detail(request, *args, **kwargs):
    id=kwargs.get("id")
    print(id)
    hotel_detail=Hotel.objects.get(id=id)
    return render(request,"hotel-detail.html",{"hotels":hotel_detail})

@signin_required
def delete_hotel(request,*args,**kwargs):
    print(request.user.is_authenticated)
    id=kwargs.get("id")
    hotel=Hotel.objects.get(id=id).delete()
    return redirect("list-hotel")

# def add_room(request):
#     if request.method == "GET":
#         form = forms.AddRoomForm()
#         return render(request, "add-room.html", {"form": form})
#     if request.method == "POST":
#         form = forms.AddRoomForm(request.POST)
#         if form.is_valid():
#             form.cleaned_data["hotel"] = Hotel.objects.get(owner_name=request.user)
#             Room.objects.create(**form.cleaned_data)
#             # form.instance.user=request.user
#             # form.save()
#             messages.success(request, "Room added succesfully")
#         return redirect("list-room")
#     else:
#         messages.error(request, "failed to add")
#     return render(request, "add-room.html", {"form": form})

def add_room(request,*args,**kwargs):
    id=kwargs.get("id")
    hotel=Hotel.objects.get(id=id)
    form =forms.AddRoomForm()
    if request.method == "POST":
        form = forms.AddRoomForm(request.POST)
        if form.is_valid():
            form.cleaned_data["hotel"] = hotel
            Room.objects.create(**form.cleaned_data)
            # form.save()
            # form.cleaned_data["theater"]=Theater.objects.get(owner=request.user)  #For 1 to 1 User
            # Screen.objects.create(**form.cleaned_data)
            messages.success(request, "Room added succesfully")
            return redirect("list-room")
        else:
            messages.success(request, "Room adding Failed")
            return render(request, "add-room.html", {"form": form})
    return render(request, "add-room.html", {"form": form})


    # if request.method == "GET":
    #     form = forms.AddRoomForm()
    #     return render(request, "add-room.html", {"form": form})
    # if request.method == "POST":
    #      form=forms.AddRoomForm(request.POST)
    #      if form.is_valid():
    #         form.instance.user=request.user
    #         form.save()
    #         messages.success(request,"Room added succesfully")
    #         return redirect("list-room")
    # else:
    #     messages.error(request,"failed to add")
    # return render(request, "add-room.html", {"form":form})

def list_room(request):
    room_list = Room.objects.all()
    return render(request, "list-room.html", {"room": room_list})

def edit_room(request,*args,**kwargs):
    if request.method == "GET":
        id=kwargs.get("id")
        room=Room.objects.get(id=id)
        form=forms.EditRoomForm(instance=room) #blank form alla eth todonte instance vachano form initialize cheyende ath
        return render(request,"edit-room.html",{"form":form})
    if request.method == "POST":
        id= kwargs.get("id")
        room =Room.objects.get(id=id)
        form=forms.EditRoomForm(request.POST,instance=room) #update aanenkil mention cheyanam instance
        if form.is_valid():
            form.save()
            msg="Room details has been updated"
            messages.success(request,msg) #to show messages  messages.add_message(request,msg content)
            return redirect("list-room")
        else:
            msg="room update failed"
            messages.error(request,msg)
            return render(request, "edit.html", {"form": form})

def delete_room(request,*args,**kwargs):
    print(request.user.is_authenticated)
    id=kwargs.get("id")
    room=Room.objects.get(id=id).delete()
    return redirect("list-room")
