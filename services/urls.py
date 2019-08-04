from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from .views import DashboardView
from . import views

<<<<<<< HEAD
urlpatterns = [
<<<<<<< HEAD
=======
>>>>>>> ef13e9b
   
urlpatterns = [
    path('', service  , name='services'),
    
    path('get_data/', get_data  , name='get_data'),
    
    path('create-service/', create_service  , name='create-service'),
    path('my-services/', my_services  , name='my_services'),
<<<<<<< HEAD
    re_path('my_services/(?P<pk>\d+)', my_services_detail  , name='my_services_detail'),
=======
	path('home',views.home,name='home'),
    path('login',view=LoginView.as_view(template_name="services/login.html",redirect_authenticated_user=True),name='login'),
    path('logout',view=LogoutView.as_view(),name='logout'),
    path('dashboard',view=DashboardView.as_view(),name='dashboard'),
    path('register',views.register,name='register'),

>>>>>>> pre-prod
=======

    re_path(r'^(?P<pk>\d+)/$', service_detail ,  name = 'service_detail'),
	
	re_path(r'my_services/(?P<pk>\d+)/$', my_services_detail  , name='my_services_detail'),
	re_path(r'my_services/del/(?P<pk>\d+)/$', service_del  , name='my_services_del'),

>>>>>>> ef13e9b
]