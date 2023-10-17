from django.shortcuts import render

from .models import District

def extras(request):
    districts = District.objects.all()
    return {'districts': districts}


