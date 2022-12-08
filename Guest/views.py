from django.shortcuts import render, redirect

# Create your views here.
from Hotel import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from Hotel.models import *
from Hotel.decorators import *
import datetime
from datetime import timedelta

@signin_required
@guest_login
def guest_home(request):
    hotel_view = Hotel.objects.all()
    return render(request, "dashboard.html", {"hot": hotel_view})


@signin_required
@guest_login
def view_room(request, id):
    hotel_name = Hotel.objects.get(id=id)
    rooms = Room.objects.filter(hotel=hotel_name, availability="Active")
    return render(request, "view-room.html", {"rooms": rooms})

@signin_required
@guest_login
def booking_view(request, id):
    room = Room.objects.get(id=id)
    form = forms.BookingForm()
    if request.method == "POST":
        form = forms.BookingForm(request.POST)
        if form.is_valid():
            if form.cleaned_data["occupancy_adult"]<=room.occupancy_adult and form.cleaned_data["occupancy_child"]<=room.occupancy_child:
                pass
            else:
                messages.error(request, "occupancy out of limit")
                return render(request, "guest-booking.html", {"form": form})
            form.cleaned_data["no_of_days"] = (
                    form.cleaned_data["stay_end_date"] - form.cleaned_data["stay_start_date"]).days
            form.cleaned_data["total"] = (form.cleaned_data["occupancy_adult"] * room.price_of_adult) * \
                                         form.cleaned_data['no_of_days'] + (form.cleaned_data[
                                                                                "occupancy_child"] * room.price_of_child) * \
                                         form.cleaned_data['no_of_days']

            if datetime.date.today() <= form.cleaned_data["stay_start_date"] < form.cleaned_data["stay_end_date"]:
                pass
            else:
                messages.error(request,"invalid date")
                return render(request, "guest-booking.html", {"form": form})
            start_date=request.POST['stay_start_date']
            end_date=request.POST['stay_start_date']
            if PerDayBooking.objects.filter(bookingss__room=room,status__in=('pending','active'),date__range=[start_date,end_date]).exists():

                messages.warning(request, "Sorry This Room is unavailable for Booking")
                return redirect("guest-home")
            else:
                pass


            form.cleaned_data["guest"] = request.user
            form.cleaned_data["room"] = room



            Bookings1=Booking.objects.create(**form.cleaned_data)


            messages.success(request, "Booking added sucessfully")
            return redirect("guest-booking-list")
        else:
            messages.success(request, "booking adding Failed")
            return render(request, "guest-booking.html", {"form": form})
    return render(request, "guest-booking.html", {"form": form})


@signin_required
@guest_login
def guest_booking_list(request):
    try:
        bookings = request.user.booking_set.all()
        return redirect("guest-booking-list", {"bookings": bookings})

    except:
        return render(request, "list-booking.html", {"bookings": bookings})

@signin_required
@guest_login
@signin_required
def logout_view(request):
    logout(request)
    return redirect("signin")


@signin_required
@guest_login
def guest_edit_booking_view(request, *args, **kwargs):

        if request.method == "GET":
            id = kwargs.get("id")
            bookingss = Booking.objects.get(id=id, status="Pending")
            form = forms.GuestEditBookingForm(instance=bookingss)
            return render(request, "guest-edit-booking.html", {"form": form})
        if request.method == "POST":
            id = kwargs.get("id")
            bookingss = Booking.objects.get(id=id, status="Pending")

            form = forms.GuestEditBookingForm(request.POST, instance=bookingss)
            if form.is_valid():
                if datetime.date.today() <= form.cleaned_data["stay_start_date"] < form.cleaned_data["stay_end_date"]:
                    pass
                else:
                    messages.error(request, "invalid date")
                    return render(request, "guest-edit-booking.html", {"form": form})
                if form.cleaned_data["occupancy_adult"] <= bookingss.room.occupancy_adult and form.cleaned_data[
                    "occupancy_child"] <= bookingss.room.occupancy_child:
                    pass
                else:
                    messages.error(request, "occupancy out of limit")
                    return render(request, "guest-edit-booking.html", {"form": form})
                for each_booking in Booking.objects.all():

                    if str(each_booking.stay_start_date) < str(request.POST['stay_start_date']) and str(
                            each_booking.stay_end_date) < str(request.POST['stay_start_date']):
                        pass
                    elif str(each_booking.stay_start_date) > str(request.POST['stay_end_date']) and str(
                            each_booking.stay_end_date) > str(request.POST['stay_end_date']):
                        pass
                    else:
                        messages.warning(request, "Sorry This date have existing bookings")
                        return redirect("guest-booking-list")
                form.save()
                msg = "Booking  has been updated"
                messages.success(request, msg)
                return redirect("guest-home")
            else:
                msg = "Booking status update failed"
                messages.error(request, msg)
                return render(request, "guest-edit-booking.html", {"form": form})


@signin_required
@guest_login
def delete_booking(request, *args, **kwargs):
    id = kwargs.get("id")
    Booking.objects.get(id=id).delete()
    return redirect("guest-booking-list")

@signin_required
@guest_login
def your_bookings_room(request,id):
    room = Room.objects.get(id=id)
    bookings = request.user.booking_set.filter(room=room).all()
    return render(request, "view-booking.html", {"viewbookings": bookings})

# @signin_required
# @guest_login
# def perdaybooking_list(request,id):
#     b = Booking.objects.get(id=id)
#     perday = PerDayBooking.objects.filter(bookingss=b,bookingss__status="Accepted")
#     return render(request, "perday-list.html", {"perday":perday})
#
# @signin_required
# @guest_login
# def vacate(request,id):
#     book = PerDayBooking.objects.get(id=id)
#     book.status = "vacated"
#     book.delete()
#     messages.success(request, "Room vacated")
#     return redirect("guest-home")


