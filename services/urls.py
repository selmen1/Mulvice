from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from .views import DashboardView
from . import views

urlpatterns = [
	path('home',views.home,name='home'),
    path('login',view=LoginView.as_view(template_name="services/login.html",redirect_authenticated_user=True),name='login'),
    path('logout',view=LogoutView.as_view(),name='logout'),
    path('dashboard',view=DashboardView.as_view(),name='dashboard'),
    path('register',views.register,name='register'),

]