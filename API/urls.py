from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path , include
from .views import *

urlpatterns = [
	# path('profile/(?P<pk>\d+)/' , ProfileDetail.as_view() , name='jsonprofile'),
	path('profile' , data_list.as_view() , name='jsonprofile'),

]

