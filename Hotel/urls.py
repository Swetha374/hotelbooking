from django.urls import path
from Hotel import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path("login/",views.login_view,name="signin"),
    path("guest/register/",views.registration,name="guest-reg"),
    path("register/",views.hotel_registration,name="hotel-reg"),
    path("home/",views.hotel_home,name="hotel-home"),
    path("list/",views.list_hotel,name="list-hotel"),
    path("details/<int:id>",views.hotel_detail,name="hotel-detail"),
    path("remove/<int:id>",views.delete_hotel,name="delete-hotel"),
    path("add/room/",views.add_room,name="add-room"),
    path("list/room/", views.list_room, name="list-room"),
    path("room/edit/<int:id>",views.edit_room,name="edit-room"),
    path("remove/room/<int:id>", views.delete_room, name="delete-room"),



]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)