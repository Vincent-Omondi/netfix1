# users/urls.py

from django.urls import path
# from django.contrib.auth import views
from .forms import UserLoginForm
from . import views as v

app_name = 'users' # added this line, I'm yet to know what it mean

urlpatterns = [
    path('', v.register, name='register'),
    path('company/', v.CompanySignUpView.as_view(), name='register_company'),
    path('customer/', v.CustomerSignUpView.as_view(), name='register_customer'),
    path('login/', v.loginUserView, name='login_user'),
    path('dashboard/', v.user_dashboard, name='dashboard'),
    path('profile/<str:username>/', v.profile, name='profile'),
]
