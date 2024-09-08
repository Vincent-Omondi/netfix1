# users/views.py

from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.decorators import login_required
from .forms import CustomerSignUpForm, CompanySignUpForm, UserLoginForm
from .models import User, Customer, Company 

def register(request):
    return render(request, 'users/register.html')

class CustomerSignUpView(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'users/register_customer.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('users:dashboard')

class CompanySignUpView(CreateView):
    model = User
    form_class = CompanySignUpForm
    template_name = 'users/register_company.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'company'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('users:dashboard')

@csrf_exempt
def loginUserView(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            try:
                user = User.objects.get(email=email)
                authenticated_user = authenticate(request, username=email, password=password)
                
                # print(f"User found: {user}")  # debugging line
                # print(f"Password provided: {password}")  # debugging line 
                # print(f"Authentication result: {authenticated_user}")  # debugging line
                
                if authenticated_user is not None:
                    login(request, authenticated_user)
                    return redirect('users:dashboard')  # Make sure this URL name is defined in your urls.py
                else:
                    messages.error(request, f"Authentication failed for user: {email}")
            except User.DoesNotExist:
                messages.error(request, "User does not exist.")
        else:
            messages.error(request, "Form is not valid.")
    else:
        form = UserLoginForm()
    
    return render(request, 'users/login.html', {'form': form})

@login_required
def user_dashboard(request):
    if hasattr(request.user, 'customer'):
        return customer_dashboard(request)
    elif hasattr(request.user, 'company'):
        return company_dashboard(request)
    else:
        # Handle unexpected user type
        return redirect('main:home')

@login_required
def customer_dashboard(request):
    customer = request.user.customer
    # Add logic to get customer's requested services
    context = {
        'customer': customer,
        # Add requested services to context
    }
    return render(request, 'users/customer_dashboard.html', context)

@login_required
def company_dashboard(request):
    company = request.user.company
    # Add logic to get company's provided services
    context = {
        'company': company,
        # Add provided services to context
    }
    return render(request, 'users/company_dashboard.html', context)