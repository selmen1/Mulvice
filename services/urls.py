from django.contrib import admin
from django.urls import path ,re_path , include
from .views import *

urlpatterns = [
    path('tous/', all_services , name='all_services'),
    path('devenir_un_mulvice/', create_service , name='create_service'),
]