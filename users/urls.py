# users/urls.py

from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    # Registration URLs
    path('', views.register, name='register'),
    path('company/', views.CompanySignUpView.as_view(), name='register_company'),
    path('customer/', views.CustomerSignUpView.as_view(), name='register_customer'),
    
    # Authentication URL
    path('login/', views.loginUserView, name='login_user'),
    
    # Profile URL
    path('profile/<str:username>/', views.profile, name='profile'),
]