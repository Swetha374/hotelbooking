from rest_framework import generics
from hotelapi.serializers import *
from Hotel.models import *
from Admin.models import *
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from rest_framework import authentication,permissions
from rest_framework.response import Response
from rest_framework import status
from hotelapi.permissions import IsHotelCreateAccess

from django.contrib.auth import authenticate, login, logout




class RegisterationView(generics.CreateAPIView):
    serializer_class=RegisterationSerializer
    queryset=User.objects.all()


class LoginView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def create(self, request,*args,**kwargs):
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid():
            uname = request.data['username']
            pwd = request.data["password"]
            user = authenticate(username=uname, password=pwd)
            print(user)
            if user:
                login(request, user)
                if request.user.is_superuser: 
                    return Response({'message': 'Admin Login Successfully'}, status=status.HTTP_200_OK)
                if request.user.usertype == 'Hotel':
                    return Response({'message': 'Hotel Login Successfully',}, status=status.HTTP_200_OK)

                if request.user.usertype == 'Guest':
                    return Response({'message': 'Guest Login Successfully', }, status=status.HTTP_200_OK)

            else:
                return Response({'message':'you must register'},status=status.HTTP_404_NOT_FOUND)
            


class HotelAddingView(generics.CreateAPIView):
    queryset=Hotel.objects.all()
    serializer_class=HotelAddingSerializer
    permission_classes=[permissions.IsAuthenticated]
    # permission_classes=(permissions.IsAuthenticated,IsHotelCreateAccess)

    def create(self, request, *args, **kwargs): 
        serializer = self.serializer_class(data=request.data) 
        if serializer.is_valid(raise_exception=True): 
            if request.user.usertype=='Hotel':
                serializer.save(owner_name=request.user)
                print(request.user.usertype)
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'message':'you must register as hotel'},status=status.HTTP_400_BAD_REQUEST)


  