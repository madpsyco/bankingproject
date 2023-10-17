from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth import authenticate

# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        print(user)
        if user is not None:
            auth.login(request,user)
            return render(request,'base.html')
            
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        try:
            user_none=User.objects.get(username=username)
        except User.DoesNotExist:
            user_none=None
        if password != cpassword:
            messages.success(request,"plaese check your password")
        elif user_none is None:
            user=User.objects.create_user(username=username,password=password)
            user.save()
            return render(request,'login.html')
        else:
            messages.success(request,'username already taken')
    return render(request,'register.html')


def formsuccess(request):
    return render(request,'formsuccess.html')