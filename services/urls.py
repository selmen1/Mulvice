from django.contrib import admin
from django.urls import path ,re_path , include
from .views import *

   
urlpatterns = [
    
    
    path('get_data/', get_data  , name='get_data'),
    
    path('create-service/', create_service  , name='create-service'),
    path('my-services/', my_services  , name='my_services'),
    path('contact_us/', contact_us  , name='contact_us'),

    re_path(r'^(?P<pk>\d+)/$', service_detail ,  name = 'service_detail'),
	
	re_path(r'my-services/(?P<pk>\d+)/$', my_services_detail  , name='my_services_detail'),
	re_path(r'my-services/del/(?P<pk>\d+)/$', service_del  , name='my_services_del'),

]