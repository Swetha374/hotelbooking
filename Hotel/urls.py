from django.urls import path
from Hotel import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path("login/",views.login_view,name="signin"),
    path("register/",views.registration,name="guest-reg"),
    path("hotel/register/",views.hotel_registration,name="hotel-reg"),
    # path("hotel/home/",views.hotel_home,name="hotel-home"),
    path("hotel/home/",views.list_hotel,name="hotel-home"),
    path("details/<int:id>",views.hotel_detail,name="hotel-detail"),
    path("remove/<int:id>",views.delete_hotel,name="delete-hotel"),
    path("add/room/<int:id>",views.add_room,name="add-room"),
    path("list/room/<int:id>", views.list_room, name="list-room"),
    path("room/edit/<int:id>",views.edit_room,name="edit-room"),
    path("remove/room/<int:id>", views.delete_room, name="delete-room"),
    path("list/bookings/", views.booking_pending_list_view, name="booking-list"),
    path("list/bookings/active/", views.booking_active_list_view, name="active-booking-list"),
    path("edit/booking/<int:id>", views.edit_booking_view, name="edit-booking-hotel"),
    path("booking/accept/<int:id>", views.accept_booking, name="accept"),
    path("booking/reject/<int:id>", views.reject_booking, name="reject"),
    path("booking/complete/<int:id>", views.completeperdaybooking, name="complete"),
    path("booking/active/<int:id>", views.Activeperdaybooking, name="active"),
    path("delete/pending/booking/<int:id>", views.delete_perday_booking, name="del"),
    path("delete/booking/<int:id>", views.delete_booking_hotel, name="delete-booking-hotel"),
    path("hotel/book/room/<int:id>/", views.owner_booking_view, name="owner-booking"),
    path("list/bookings/room/<int:id>", views.view_room_bookings, name="view-room-bookings"),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)