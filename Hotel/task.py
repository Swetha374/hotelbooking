import os
from HotelBooking.celery import app
from celery import shared_task
from Hotel.models import *
from django.conf import settings
from django.core.mail import EmailMessage


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