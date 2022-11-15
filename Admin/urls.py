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
from django.urls import path
from Admin import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
path("index",views.admin_home,name="admin-home"),
path("delete/hotel/<int:id>",views.admin_delete_hotel,name="admin-delete-hotel"),
path("list/rooms/<int:id>",views.room_admin,name="rooms-admin"),
path("add/room/<int:id>",views.room_add,name="room-add"),
path("edit/room/<int:id>",views.admin_edit_room,name="room-edit"),
path("delete/room/<int:id>",views.admin_delete_room,name="admin-delete-room"),


]