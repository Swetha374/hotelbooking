from django.shortcuts import redirect
from django.contrib import messages

def signin_required(fn):
      def wrapper(request,*args,**kwargs): #inner fn
        if not request.user.is_authenticated:
            messages.error(request,"you must login")
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
      return wrapper


def hotel_login(fn):
    def hotel_wrapper_fn(request, *args, **kwargs):
        if not request.user.usertype=="Hotel":
            messages.error(request, "you must login as hotel")
            return redirect("signin")
        else:
            return fn(request, *args, **kwargs)

    return hotel_wrapper_fn

def guest_login(fn):
    def guest_wrapper_fn(request, *args, **kwargs):
        if not request.user.usertype=="Guest":
            messages.error(request, "you must login as guest")
            return redirect("signin")
        else:
            return fn(request, *args, **kwargs)

    return guest_wrapper_fn

def admin_login(fn):
    def admin_wrapper_fn(request, *args, **kwargs):
        if not request.user.is_superuser:
            messages.error(request, "you must login as admin")
            return redirect("signin")
        else:
            return fn(request, *args, **kwargs)

    return admin_wrapper_fn

