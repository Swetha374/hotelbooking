"""HotelBooking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from Guest import views

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

   path("dashboard/",views.guest_home,name="guest-home"),
   path("logout",views.logout_view,name="logout"),
   path("view/rooms/<int:id>/", views.view_room, name="view-room"),
   path("book/room/<int:id>/",views.booking_view,name="guest-booking"),
   path("list/booking/",views.guest_booking_list,name="guest-booking-list"),
   path("edit/booking/<int:id>/",views.guest_edit_booking_view,name="guest-edit-booking"),
   path("list/delete/booking/<int:id>",views.delete_booking,name="delete-booking"),
   path("view/booking/<int:id>",views.your_bookings_room,name="guest-view-booking"),


] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)