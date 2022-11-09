from django.urls import path
from Hotel import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path("login",views.login_view,name="signin"),
    path("hotel/register",views.hotel_registration,name="hotel-reg"),




]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)