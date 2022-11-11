from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser,PermissionsMixin,AbstractUser
from django.db import models
from django.contrib.auth.models import UserManager

USER_TYPE=(
        ("Hotel","Hotel"),
        ("Guest","Guest"),
         )
GENDER=(
    ("male","male"),
    ("female","female"),
    ("others","others")
)

class Manager(UserManager):

    def create_superuser(self,username,email,password,**extra_fields):
        extra_fields['is_superuser'] = True
        super(Manager, self).create_superuser(username,email,password,**extra_fields)


class User(AbstractUser):
    # is_admin = models.BooleanField("Is admin", default=False)
    # is_hotel = models.BooleanField("Is hotel", default=False)
    # is_guest = models.BooleanField("Is guest", default=False)
    name = models.CharField(max_length=200, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER, null=True)
    mobile = models.CharField(max_length=12, null=True)
    owner_name = models.CharField(max_length=50)
    owner_image = models.ImageField(upload_to="owner_images", null=True, blank=True)
    owner_mobile = models.CharField(max_length=12)
    usertype = models.CharField(choices=USER_TYPE, max_length=50, default="Guest")



    objects=Manager()