import datetime
from Hotel.models import *

def check_availability(room,stay_start_date,stay_end_date):
    avail_list=[]
    bookings_li=Booking.objects.filter(room=room)
    for booking in bookings_li:
        if booking.stay_start_date > stay_end_date or booking.stay_end_date < stay_start_date:
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)
