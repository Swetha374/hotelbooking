from django.shortcuts import render, redirect
from Hotel.decorators import signin_required

@signin_required
def admin_home(request):
    return render(request,"index.html")