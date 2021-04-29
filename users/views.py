from django.shortcuts import render,redirect
from django.contrib.auth import logout,login,authenticate
# Create your views here.
from django.contrib import messages
from .models import CustomUser
def loginProcess(request):
    if request.method == "POST":
        email=request.POST['email']
        password=request.POST['password']
        user =authenticate(username=email,password=password)
        if user:
            login(request,user)
            messages.success(request,'Successfully Logged in')
            return redirect("Home")
        else:
            messages.error(request,'You are not Registered')
    return render(request,"login.html")


def registerProcess(request):
    if request.method == "POST":
        firstname=request.POST['First_Name']
        lastname=request.POST['Last_Name']
        username=request.POST['email']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['cpassword']

        if password == confirm_password:
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request,'Username already exists')
                return redirect('register')
            else:
                if CustomUser.objects.filter(email=email).exists():
                    messages.error(request,'Email already exists')
                    return redirect('register')
                else:
                    user=CustomUser.objects.create_user(username=username,email=email,password=password,first_name=firstname,last_name=lastname)

                    user.save()
                    login(request,user)
                    messages.success(request,'Successfully Registered')
                    return redirect('Home')
        else:
            messages.error(request,'Please Enter same input in Password and Confirm Password')
            return redirect('register')
    return render(request,"register.html")

def logoutProcess(request):
    logout(request)
    messages.success(request,"You are Successfully Logged Out")
    return redirect("Home")
