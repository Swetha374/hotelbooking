from django.contrib import admin
from Hotel.models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(PerDayBooking)

