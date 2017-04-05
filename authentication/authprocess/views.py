from django.shortcuts import render,redirect
from authprocess.models import *
from django.contrib.auth.hashers import make_password,check_password


    
def homepage(request):
    if(request.session.has_key("username")):
        return render(request,"profile.html",{"username":request.session["username"]})
    else:
       
        return redirect("register")

def register(request):
    if request.method=="POST":
        user=request.POST["username"]
        passwd=request.POST["password"]
        if(users.objects.filter(username=user).exists()):
            message="username already exist"
            return render(request,"register.html",{"message":message})
        else:
            users.objects.create(username=user,password=make_password(passwd))
            message="You have registered now login"
            return render(request,"login.html",{"message":message})
    else:
        return render(request,"register.html",{})
    

    
def login(request):
    if(request.method=="POST"):
        loguser=request.POST["username"]
        logpass=request.POST["password"]
        if(users.objects.filter(username=loguser).exists()):
            check=users.objects.get(username=loguser)
            if check_password(logpass,check.password) and check.is_active:
                request.session["username"]=loguser
                return redirect("home")
            else:
                message="invalid username or password"
                return render(request,"login.html",{"message":message})
        else:
            message="invalid username or password"
            return render(request,"login.html",{"message":message})
    else:
        return render(request,"login.html",{})
    
def logout(request):
    if "username" in request.session.keys():
        del request.session["username"]
        request.session.set_expiry(-2);
        message="you have sucessfully logged out"
        return render(request,"login.html",{"message":message})
    else:
        return redirect("login")
    
           
# Create your views here.
