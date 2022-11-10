from django.urls import path
from Hotel import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path("login",views.login_view,name="signin"),
    path("register",views.hotel_registration,name="hotel-reg"),
    path("guest/register",views.guest_registration,name="guest-reg"),
    path("home",views.hotel_home,name="hotel-home"),





]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)