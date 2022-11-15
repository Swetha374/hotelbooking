from django.shortcuts import render, redirect
from Hotel.decorators import *
from django.contrib import messages
from Hotel.models import *
from Hotel.forms import AddRoomForm,EditRoomForm

@signin_required
@admin_login
def admin_home(request):
     hotel_view = Hotel.objects.all()
     return render(request, "index.html", {"hotels": hotel_view})

@signin_required
@admin_login
def room_admin(request,id):
    all_hotel = Hotel.objects.get(id=id)
    rooms= Room.objects.filter(hotel=all_hotel)
    return render(request, "rooms-admin.html", {"roomss": rooms})

@signin_required
@admin_login
def room_add(request, *args, **kwargs):
        id = kwargs.get("id")
        hotel = Hotel.objects.get(id=id)
        form = AddRoomForm()
        if request.method == "POST":
            form = AddRoomForm(request.POST)
            if form.is_valid():
                form.cleaned_data["hotel"] = hotel
                Room.objects.create(**form.cleaned_data)
                messages.success(request, "Room added succesfully")
                return redirect("admin-home")
            else:
                messages.success(request, "Room adding Failed")
                return render(request, "room-add.html", {"form": form})
        return render(request, "room-add.html", {"form": form})

@signin_required
@admin_login
def admin_delete_hotel(request, *args, **kwargs):
    print(request.user.is_authenticated)
    id = kwargs.get("id")
    hotel = Hotel.objects.get(id=id).delete()
    return redirect("admin-home")

@signin_required
@admin_login
def admin_edit_room(request, *args, **kwargs):
        if request.method == "GET":
            id = kwargs.get("id")
            room = Room.objects.get(id=id)
            form = EditRoomForm(instance=room)
            return render(request, "room-edit.html", {"form": form})
        if request.method == "POST":
            id = kwargs.get("id")
            room = Room.objects.get(id=id)
            form = EditRoomForm(request.POST, instance=room)
            if form.is_valid():
                form.save()
                msg = "Room details has been updated"
                messages.success(request, msg)
                return redirect("admin-home")
            else:
                msg = "room update failed"
                messages.error(request, msg)
                return render(request, "room-edit.html", {"form": form})


@signin_required
def admin_delete_room(request, *args, **kwargs):
    print(request.user.is_authenticated)
    id = kwargs.get("id")
    room = Room.objects.get(id=id).delete()
    messages.success(request, "Room deleted")
    return redirect("admin-home")