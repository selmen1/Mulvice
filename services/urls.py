from django.contrib import admin
from django.urls import path ,re_path , include
from .views import *

   
urlpatterns = [
    path('', service  , name='services'),
    
    path('get_data/', get_data  , name='get_data'),
    
    path('create-service/', create_service  , name='create-service'),
    path('my-services/', my_services  , name='my_services'),

    re_path(r'^(?P<pk>\d+)/$', service_detail ,  name = 'service_detail'),
	
	re_path(r'my_services/(?P<pk>\d+)/$', my_services_detail  , name='my_services_detail'),
	re_path(r'my_services/del/(?P<pk>\d+)/$', service_del  , name='my_services_del'),

]