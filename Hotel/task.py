import os
from HotelBooking.celery import app
from celery import shared_task
from Hotel.models import *
from django.conf import settings
from django.core.mail import EmailMessage
from datetime import timedelta
import datetime



@shared_task(bind=True)
def test_func(request,id):
    book = Booking.objects.get(id=id)
    to = [book.guest.email]
    subject = "Booking Accepted"
    message = "Your booking has been accepted successfully"
    imagespath = book.room.hotel.image
    email_from = settings.EMAIL_HOST_USER
    email = EmailMessage(subject, message, email_from, to)
    email.attach_file(os.path.join(settings.BASE_DIR, 'media', str(imagespath)))
    email.send()

    return "Done"

@shared_task(bind=True)
def per_task(id):
    booking=PerDayBooking.objects.all()
    for b in booking:
        if b.date==datetime.date.today():
            b.status="active"
            b.save()
            
        elif b.date==datetime.date.today()-datetime.timedelta(days=1):
            b.status="completed"
            b.save()
            
    return "Task completed"