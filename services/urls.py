from django.contrib import admin
from django.urls import path ,re_path , include
from .views import *

urlpatterns = [
   
    path('', service  , name='services'),
    path('create-service/', create_service  , name='create-service'),
    re_path('(?P<pk>\d+)/', service_detail ,  name = 'service_detail'),
    path('my-services/', my_services  , name='my_services'),
    re_path('my_services/(?P<pk>\d+)', my_services_detail  , name='my_services_detail'),
]