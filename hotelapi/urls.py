from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include

# from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from hotelapi import views

urlpatterns = [
    path("register/",views.RegisterationView.as_view(),name="reg"),
    path("login/user/",views.LoginView.as_view(),name="loginn"),
    path("hotel/",views.HotelAddingListingView.as_view(),name="add-hot"),
    path("hotel/detail/<int:id>/",views.HotelDetailUpdateView.as_view(),name="det-hot"),
    path("hotel/delete/<int:id>/",views.HotelDeleteView.as_view(),name="del-hot"),
    path("hotel/<int:id>/room/",views.RoomAddListView.as_view(),name="add-list-room"),
    path("token/",TokenObtainPairView.as_view()),
    path("token/refresh/",TokenRefreshView.as_view()),
   
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
