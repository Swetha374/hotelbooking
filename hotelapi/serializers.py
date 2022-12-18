from rest_framework import serializers
from django import forms
from hotelapi.permissions import IsHotelCreateAccess
from Hotel.models import *
from Admin.models import *

class RegisterationSerializer(serializers.ModelSerializer):
      class Meta:
        model=User
        fields=[
            "name",
            "dob",
            "gender",
            "mobile",
            "email",
            "usertype",
            "username",
            "password"

        ]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}),
            "password": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "password"}),
        }
        

      def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
  username = forms.CharField(widget=forms.TextInput( attrs={"class": "form-control"}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))       


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Hotel
        fields=["id",
                "hotel_name",
                "image",
                "address",
                "location",
                "star_rating",
               

                ]
        
    # def create(self, validated_data):
    #     if self.context['request'].user.usertype=="Hotel":
    #         user=self.context['request'].user
    #         hotel=Hotel.objects.create(**validated_data,owner_name=user)
    #         print(hotel)
    #         return hotel     
        
class RoomSerializer(serializers.ModelSerializer):
  class Meta:
    model=Room
    # fields="__all__"
    exclude = ("hotel",)


  def create(self, validated_data):
            user=self.context['request'].user 
            hotel_id=self.context['hotel_id']
            room=Room.objects.create(**validated_data,hotel_id=hotel_id)
            return room  
            