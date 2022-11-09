from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser,AbstractUser
from django.core.validators import MaxValueValidator,MinValueValidator

class BaseUser(AbstractBaseUser):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    dob=models.DateField()
    OPTIONS=(
        ("male","male"),
        ("female","female"),
        ("others","others")
    )
    gender=models.CharField(max_length=20,choices=OPTIONS)
    mobile=models.CharField(max_length=12)
    email=models.EmailField(verbose_name='email address',max_length=200,unique=True)
    address=models.TextField(max_length=120)
    CHOICE=(
        ("Admin","Admin"),
        ("Hotel","Hotel"),
        ("Guest","Guest")
    )
    type_of_user=models.CharField(max_length=50,choices=CHOICE)
    USERNAME_FIELD='email'


class Hotel(models.Model):

    hotel_name= models.CharField(max_length=120,unique=True)
    image=models.ImageField(upload_to="images",null=True)
    address=models.TextField(max_length=120)
    location=models.CharField(max_length=50)
    star_rating=models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    owner_name=models.CharField(max_length=50)
    owner_image=models.ImageField(upload_to="owner_images",null=True,blank=True)
    owner_email=models.EmailField(null=True,unique=True)
    owner_mobile=models.CharField(max_length=12)
    CHOICE = (
        ("Admin", "Admin"),
        ("Hotel", "Hotel"),
        ("Guest", "Guest")
    )
    type_of_user = models.CharField(max_length=50, choices=CHOICE,default="Guest")

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
    guest=models.ForeignKey(BaseUser,on_delete=models.CASCADE)
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    stay_start_date=models.DateField()
    stay_end_date=models.DateField()
