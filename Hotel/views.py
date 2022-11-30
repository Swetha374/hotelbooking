from django.shortcuts import render, redirect

# Create your views here.
from Hotel import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from Hotel.models import *
from Hotel.decorators import *
import datetime
from datetime import timedelta
from django.db.models import Sum,Count



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
                    return redirect("guest-home")
        else:
            messages.error(request, "invalid username or password")
        messages.error(request, "please login")
        return render(request, "signin.html", {"form": form})


def hotel_registration(request):
    if request.method == "GET":
        form = forms.HotelRegistration()
        return render(request, "hotel-reg.html", {"form": form})
    if request.method == "POST":
        form = forms.HotelRegistration(request.POST, files=request.FILES)
        if form.is_valid():
            form.instance.owner_name = request.user
            form.save()
            messages.success(request, "your hotel has been added")
            return redirect("hotel-home")
    else:
        messages.error(request, "registration failed")
    return render(request, "hotel-reg.html", {"form": form})


def registration(request):
    if request.method == "GET":
        form = forms.Registration()
        return render(request, "guest-reg.html", {"form": form})

    if request.method == "POST":
        form = forms.Registration(request.POST, files=request.FILES)
        if form.is_valid():
            user = User.objects.create_user(**form.cleaned_data)
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            messages.success(request, "your account has been created")
            return redirect("signin")

    else:
        messages.error(request, "registration failed")
    return render(request, "guest-reg.html", {"form": form})


@signin_required
@hotel_login
def hotel_home(request):
    return render(request, "home.html")


@signin_required
@hotel_login
def list_hotel(request):
    hotel = request.user.hotel_set.all()
    booking_list = Booking.objects.filter(room__hotel__owner_name=request.user, status="Accepted")
    bl=booking_list.aggregate(Sum("total"))
    print(bl)
    booking_count = booking_list.count()
    pending = Booking.objects.exclude(status="Accepted").filter(room__hotel__owner_name=request.user).count()
    context = {}
    context["hotel"] = hotel
    context["count"] = booking_count
    context["pcount"] = pending
    context["total"] =bl['total__sum']

    return render(request, "home.html", context)


@signin_required
@hotel_login
def hotel_detail(request, *args, **kwargs):
    id = kwargs.get("id")
    print(id)
    hotel_detail = Hotel.objects.get(id=id)
    return render(request, "hotel-detail.html", {"hotels": hotel_detail})


@signin_required
def delete_hotel(request, *args, **kwargs):
    if not Booking.objects.filter(status="Accepted"):
        id = kwargs.get("id")
        hotel = Hotel.objects.get(id=id).delete()
        return redirect("hotel-home")
    else:
        messages.error(request, "sorry this room has active bookings  ")
        return redirect("hotel-home")


@hotel_login
def add_room(request, id):
    hotel = Hotel.objects.get(id=id)
    form = forms.AddRoomForm()
    if request.method == "POST":
        form = forms.AddRoomForm(request.POST)
        if form.is_valid():
            form.cleaned_data["hotel"] = hotel
            Room.objects.create(**form.cleaned_data)
            messages.success(request, "Room added sucessfully")
            return redirect("list-room", id=id)
        else:
            messages.success(request, "Room adding Failed")
            return render(request, "add-room.html", {"form": form})
    return render(request, "add-room.html", {"form": form})


@hotel_login
def list_room(request, id):
    try:
        hotel = Hotel.objects.get(id=id)
        room = Room.objects.filter(hotel=hotel)
        return render(request, "list-room.html", {"room": room})
    except:
        return render(request, "list-room.html")


@signin_required
@hotel_login
def edit_room(request, *args, **kwargs):
    try:
        if request.method == "GET":
            id = kwargs.get("id")
            room = Room.objects.get(id=id)
            form = forms.EditRoomForm(instance=room)
            return render(request, "edit-room.html", {"form": form})
        if request.method == "POST":
            id = kwargs.get("id")
            room = Room.objects.get(id=id)
            form = forms.EditRoomForm(request.POST, instance=room)
            if form.is_valid():
                form.save()
                msg = "Room details has been updated"
                messages.success(request, msg)
                return redirect("hotel-home")
            else:
                msg = "room update failed"
                messages.error(request, msg)
                return render(request, "edit-room.html", {"form": form})
    except:
        return render(request, "list-room.html")


@signin_required
@hotel_login
def delete_room(request, *args, **kwargs):
    print(request.user.is_authenticated)
    id = kwargs.get("id")
    room = Room.objects.get(id=id).delete()
    messages.success(request, "Room deleted")
    return redirect("hotel-home")


def owner_booking_view(request, id):
    roomm = Room.objects.get(id=id)
    status = Booking.objects.exclude(status="Accepted")
    form = forms.OwnerBookingForm()
    if request.method == "POST":
        form = forms.OwnerBookingForm(request.POST)
        if form.is_valid():
            if form.cleaned_data["occupancy_adult"] <= roomm.occupancy_adult and form.cleaned_data[
                "occupancy_child"] <= roomm.occupancy_child:
                pass
            else:
                messages.error(request, "occupancy out of limit")
                return render(request, "owner-booking.html", {"form": form})
            form.cleaned_data["no_of_days"] = (
                    form.cleaned_data["stay_end_date"] - form.cleaned_data["stay_start_date"]).days
            form.cleaned_data["total"] = (form.cleaned_data["occupancy_adult"] * roomm.price_of_adult) * \
                                         form.cleaned_data['no_of_days'] + (form.cleaned_data[
                                                                                "occupancy_child"] * roomm.price_of_child) * \
                                         form.cleaned_data['no_of_days']

            if datetime.date.today() <= form.cleaned_data["stay_start_date"] < form.cleaned_data["stay_end_date"]:
                pass
            else:
                messages.error(request, "invalid date")
                return render(request, "owner-booking.html", {"form": form})
            for each_book in Booking.objects.filter(room=roomm):
                if str(each_book.stay_start_date) < str(request.POST['stay_start_date']) and str(
                        each_book.stay_end_date) < str(request.POST['stay_start_date']):
                    pass
                elif str(each_book.stay_start_date) > str(request.POST['stay_end_date']) and str(
                        each_book.stay_end_date) > str(request.POST['stay_end_date']):
                    pass
                else:
                    messages.warning(request, "Sorry This Room is unavailable for Booking")
                    return redirect("hotel-home")

            form.cleaned_data["guest"] = request.user
            form.cleaned_data["room"] = roomm
            Booking.objects.create(**form.cleaned_data)
            messages.success(request, "Booking added sucessfully")
            return redirect("hotel-home")
        else:
            messages.success(request, "booking adding Failed")
            return render(request, "owner-booking.html", {"form": form})
    return render(request, "owner-booking.html", {"form": form})


def booking_pending_list_view(request):
    bookingslist = Booking.objects.exclude(status="Accepted").filter(room__hotel__owner_name=request.user)
    return render(request, "booking-list.html", {"bookingslist": bookingslist})



def booking_active_list_view(request,*args,**kwargs):
    active_bookings = PerDayBooking.objects.filter(bookingss__room__hotel__owner_name=request.user,bookingss__status="Accepted")
    return render(request, "active-booking.html",{"active":active_bookings})



def delete_booking_hotel(request, *args, **kwargs):
    id = kwargs.get("id")
    bookingdel = Booking.objects.get(id=id).delete()
    return redirect("booking-list")


def edit_booking_view(request, *args, **kwargs):

    # try:
    if request.method == "GET":
        id = kwargs.get("id")
        bookings = Booking.objects.get(id=id)
        form = forms.OwnerEditBookingForm(instance=bookings)
        return render(request, "edit-booking-hotel.html", {"form": form})
    if request.method == "POST":
        id = kwargs.get("id")
        bookings = Booking.objects.get(id=id)
        form = forms.OwnerEditBookingForm(request.POST,instance=bookings)
        if form.is_valid():
            form.save()
            msg = "Booking status has been updated"
            messages.success(request, msg)
            return redirect("booking-list")
        else:
            messages.error(request,"Booking status update failed")
            return render(request,"edit-booking-hotel.html", {"form":form})


# except:
#     return render(request, "booking-list.html")


def view_room_bookings(request, id):
    room = Room.objects.get(id=id)
    bookings = Booking.objects.filter(room=room,)
    return render(request, "view-room-bookings.html", {"roombookings": bookings})

def accept_booking(request,id):
    book=Booking.objects.get(id=id)
    pending= Booking.objects.exclude(status="Accepted").filter(room__hotel__owner_name=request.user)
    accepted=Booking.objects.filter(room__hotel__owner_name=request.user,status="Accepted")

    # vacated= PerDayBooking.objects.filter(status="vacated").filter(bookingss__room__hotel__owner_name=request.user)
    # accepted2=PerDayBooking.objects.filter(bookingss__room__hotel__owner_name=request.user,bookingss__status="Accepted")
    # for v,a in zip(vacated,accepted2):
    #     if str(v.date) in str(a.date):
    #         print(v.date)
    #         pass
    #     else:
    #         messages.warning(request, "Sorry This Room is already occupied")
    #         return redirect("hotel-home")

    for i,j in zip(pending,accepted):
        if str(i.stay_start_date) < str(j.stay_start_date) and str(i.stay_end_date) < str(j.stay_start_date) :
            pass
        elif str(i.stay_start_date) > str(j.stay_end_date) and str(i.stay_end_date) > str(j.stay_start_date):
            pass
        else:
            messages.warning(request, "Sorry This Room is already occupied")
            return redirect("hotel-home")
    dt = []
    for p in pending:

        for i in range((p.stay_end_date - p.stay_start_date).days + 1):
            bk = p.stay_start_date + timedelta(days=i)
            dt.append(bk)
    dt1=set(dt)
    dt2=list(dt1)
    dt2.sort()
    for d in dt2:
        PerDayBooking.objects.create(bookingss=p, date=d)

    book.status="Accepted"
    book.save()
    messages.success(request,"Booking accepted")
    return redirect("booking-list")

def reject_booking(request,id):
    book=Booking.objects.get(id=id)
    book.status="Rejected"
    book.save()
    messages.success(request,"Booking rejected")
    return redirect("booking-list")

def vacateperdaybooking(request,id):
    book = PerDayBooking.objects.get(id=id)
    book.status = "vacated"
    book.save()
    messages.success(request, "Room vacated")
    return redirect("active-booking-list")

