from django.urls import path
from credentials import views
app_name='credentials'

urlpatterns=[
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('formsuccess/',views.formsuccess,name='formsuccess'),
]