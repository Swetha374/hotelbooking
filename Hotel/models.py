from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser,AbstractUser
from django.core.validators import MaxValueValidator,MinValueValidator
from django.contrib.auth.models import UserManager

# USER_TYPE=(
#         ("Admin","Admin"),
#         ("Hotel","Hotel"),
#         ("Guest","Guest")
#     )


GENDER=(
    ("male","male"),
    ("female","female"),
    ("others","others")
)




class User(AbstractUser):
    is_admin=models.BooleanField("Is admin",default=False)
    is_hotel = models.BooleanField("Is hotel", default=False)
    is_guest = models.BooleanField("Is guest", default=False)
    name = models.CharField(max_length=200,null=True,blank=True)
    dob=models.DateField(null=True,blank=True)
    gender=models.CharField(max_length=20,choices=GENDER,null=True)
    mobile=models.CharField(max_length=12,null=True)
    email=models.EmailField(verbose_name='email address',max_length=200,unique=True)
    username= models.CharField(max_length=30, unique=True)
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)


class Hotel(models.Model):

    hotel_name= models.CharField(max_length=120)
    image=models.ImageField(upload_to="images",null=True)
    address=models.TextField(max_length=120)
    location=models.CharField(max_length=50)
    star_rating=models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    owner_name=models.CharField(max_length=50)
    owner_image=models.ImageField(upload_to="owner_images",null=True,blank=True)
    owner_email=models.EmailField(null=True)
    owner_mobile=models.CharField(max_length=12)
    is_admin = models.BooleanField("Is admin", default=False)
    is_hotel = models.BooleanField("Is hotel", default=False)
    is_guest = models.BooleanField("Is guest", default=False)
    username=models.CharField(max_length=30)
    password1=models.CharField(max_length=50)
    password2=models.CharField(max_length=50)



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
