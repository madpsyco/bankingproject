from django.urls import path
from . import views
app_name='coreapp'

urlpatterns=[
    path('',views.base,name='base'),
    path('home_view',views.home_view,name='home_view')
]