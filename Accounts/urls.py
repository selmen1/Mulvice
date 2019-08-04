
from django.urls                import path,re_path , include
from Accounts.views             import *
from services.views             import *
from django.contrib.auth.views import LoginView ,LogoutView , PasswordResetView , PasswordResetCompleteView,  PasswordChangeDoneView, PasswordResetConfirmView, PasswordResetDoneView ,PasswordChangeView

urlpatterns = [

	
    #path('', LoginView.as_view(), name='login_redirect'),
    path('login/', LoginView.as_view()  , name='login'),
    path('logout/', LogoutView.as_view() , name='logout'),
    path('reset-password/', PasswordResetView.as_view() ,  name='password_reset'),
    path('reset-password/done/', PasswordResetDoneView.as_view()  , name='password_reset_done'),
    path('reset-password/complete/', PasswordResetCompleteView.as_view()  , name='password_reset_complete'),
    re_path('reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/', PasswordResetConfirmView.as_view()  , name='password_reset_confirm'),
   	
    path('signup/', signup, name='signup'),
    re_path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
        activate, name='activate'),

    path('profile/', profile , name='profile'),


    #re_path('profile/(?P<pk>\d+)/', profile , name='profile'),

    path('change_password', change_password, name='change_password'),
   ]   