from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser,AbstractUser
from django.core.validators import MaxValueValidator,MinValueValidator
from django.contrib.auth.models import UserManager
from Admin.models import User




class Hotel(models.Model):

    hotel_name= models.CharField(max_length=120)
    image=models.ImageField(upload_to="images",null=True)
    address=models.TextField(max_length=120)
    location=models.CharField(max_length=50)
    star_rating=models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    password=models.CharField(max_length=50)
    owner_name = models.OneToOneField(User, on_delete=models.CASCADE)  # one to one relation
    username=models.CharField(max_length=50)

class Room(models.Model):
    room_name=models.CharField(max_length=20)
    OPTIONS=(
        ("Booked","Booked"),
        ("Open","Open"),

    )
    availability=models.CharField(max_length=50,choices=OPTIONS,default="Open")
    price=models.PositiveIntegerField()
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    occupancy_adult=models.PositiveIntegerField()
    occupancy_child=models.PositiveIntegerField()


class Booking(models.Model):
    OPTIONS=(
        ("Pending","Pending"),
        ("Accepted","Accepted"),
        ("Rejected","Rejected"),
        ("Expired","Expired")
    )
    status=models.CharField(max_length=50,choices=OPTIONS)
    occupancy_adult = models.PositiveIntegerField()
    occupancy_child = models.PositiveIntegerField()
    guest=models.ForeignKey(User,on_delete=models.CASCADE)
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    stay_start_date=models.DateField()
    stay_end_date=models.DateField()
