from django.shortcuts import redirect
from django.contrib import messages

def signin_required(fn):  #decorator fn recieves an argument function(viewsile all functions)
      def wrapper(request,*args,**kwargs): #inner fn
        if not request.user.is_authenticated:
            messages.error(request,"you must login")
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)

      return wrapper