from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser,AbstractUser
from django.core.validators import MaxValueValidator,MinValueValidator
from django.contrib.auth.models import UserManager
from Admin.models import User




class Hotel(models.Model):
    hotel_name= models.CharField(max_length=120,unique=True)
    image=models.ImageField(upload_to="images/",null=True)
    address=models.TextField(max_length=120)
    location=models.CharField(max_length=50)
    star_rating=models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    password=models.CharField(max_length=50)
    owner_name = models.ForeignKey(User, on_delete=models.CASCADE)  # one to one relation
    # total_bookings = models.IntegerField(default=0)
    username=models.CharField(max_length=50)

    def __str__(self):
        return self.hotel_name

class Room(models.Model):
    room_name=models.CharField(max_length=20)
    OPTIONS=(
        ("Booked","Booked"),
        ("Active","Active"),
        ("inactive","inactive")

    )
    availability=models.CharField(max_length=50,choices=OPTIONS,default="Active")
    price_of_adult=models.FloatField(default=2000.0)
    price_of_child=models.FloatField(default=1000.0)
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name="Hotel")
    occupancy_adult=models.PositiveIntegerField()
    occupancy_child=models.PositiveIntegerField()


    def __str__(self):
        return self.room_name




class Booking(models.Model):
    OPTIONS=(
        ("Pending","Pending"),
        ("Accepted","Accepted"),
        ("Rejected","Rejected"),
        ("Cancelled","Cancelled")
    )
    status=models.CharField(max_length=50,choices=OPTIONS,default="Pending")
    occupancy_adult = models.PositiveIntegerField()
    occupancy_child = models.PositiveIntegerField()
    guest=models.ForeignKey(User,on_delete=models.CASCADE)
    guest_name=models.CharField(max_length=50,default="-")
    guest_mobile=models.CharField(max_length=12, null=True,blank=True)
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    total=models.FloatField()
    stay_start_date=models.DateField()
    stay_end_date=models.DateField()
    no_of_days=models.IntegerField()

