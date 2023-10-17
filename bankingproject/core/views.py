from django.shortcuts import render, redirect
from django.shortcuts import render
from .models import Formdata


def base(request):
    return render(request, 'base.html')


# Create your views here.
def home_view(request):
    if request.method=='POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        address=request.POST.get('address')
        district=request.POST.get('district')
        branch=request.POST.get('branch')
        account=request.POST.get('account')
        atmcard=request.POST.get('atmcard')
        checkbook=request.POST.get('checkbook')
        formadd=Formdata(name=name,age=age,gender=gender,phone=phone,email=email,address=address,district=district,branch=branch,account=account,atmcard=atmcard,checkbook=checkbook)
        formadd.save()
        if formadd is not None:
            return redirect('/credentials/formsuccess')
    return render(request, "home.html")
