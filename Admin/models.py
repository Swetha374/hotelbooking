from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

class BaseUser(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    dob=models.DateField()
    option=(
        ("male","male"),
        ("female","female"),
        ("others","others")
    )
    gender=models.CharField(max_length=20,choices=option)
    mobile=models.CharField(max_length=12)
    address=models.TextField(max_length=120)
    choice=(
        ("Admin","Admin"),
        ("Hotel","Hotel"),
        ("Guest","Guest")
    )
    type_of_user=models.CharField(choices=choice)


class Hotel(models.Model):
    name=models.CharField(max_length=120)
    image=models.ImageField(upload_to="images",null=True)
    address=models.TextField(max_length=120)
    location=models.CharField(max_length=50)
    star_rating=models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    owner_name=models.CharField(max_length=50)
    owner_image=models.ImageField(upload_to="owner_images",null=True)
    owner_email=models.EmailField(blank=True)
    owner_mobile=models.CharField(max_length=12)

class Room(models.Model):
    room_name=models.CharField(max_length=20)
    options=(
        ("Booked","Booked"),
        ("Open","Open"),

    )
    availability=models.CharField(choices=options,default="Open")
    price=models.PositiveIntegerField()
    occupancy_adult=models.PositiveIntegerField()
    occupancy_child=models.PositiveIntegerField()


class Booking(models.Model):
    booking_id=models.CharField(max_length=100,primary_key=True)
    occupancy_adult = models.PositiveIntegerField()
    occupancy_child = models.PositiveIntegerField()
    guest=models.ForeignKey(BaseUser,on_delete=models.CASCADE)
    room=models.ForeignKey(Rooms,on_delete=models.CASCADE)
    stay_start_date=models.DateField()
    stay_end_date=models.DateField()






