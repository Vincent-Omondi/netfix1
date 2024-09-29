# users/views.py

# Django imports
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, get_user_model
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import PermissionDenied

# Local imports
from .forms import CustomerSignUpForm, CompanySignUpForm, UserLoginForm
from .models import User, Customer, Company
from services.models import Service, ServiceHistory

User = get_user_model()

def register(request):
    """View for choosing registration type."""
    return render(request, 'users/register.html')

class CustomerSignUpView(CreateView):
    """View for customer registration."""
    model = User
    form_class = CustomerSignUpForm
    template_name = 'users/register_customer.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class CompanySignUpView(CreateView):
    """View for company registration."""
    model = User
    form_class = CompanySignUpForm
    template_name = 'users/register_company.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'company'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

@csrf_exempt
def loginUserView(request):
    """View for user login."""
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.GET.get('next', '/')
            return redirect(next_url)
        else:
            # Generic error message for all login failures
            messages.error(request, "Invalid login credentials. Please try again.")
    else:
        form = UserLoginForm()
   
    return render(request, 'users/login.html', {'form': form})

@login_required
def profile(request, username):
    """View for user profile."""
    user = get_object_or_404(User, username=username)
    
    # Access control
    if request.user != user:
        if user.is_customer and not request.user.is_company:
            raise PermissionDenied
        elif user.is_company and request.user.is_company:
            raise PermissionDenied

    context = {'user': user}

    try:
        if user.is_customer:
            service_history = ServiceHistory.objects.filter(customer=user.customer).order_by('-request_date')
            context['sh'] = service_history
            context['age'] = user.customer.age()
        elif user.is_company:
            services = Service.objects.filter(company=user.company).order_by('-date')
            context['services'] = services
    except (Customer.DoesNotExist, Company.DoesNotExist):
        messages.error(request, "User profile is incomplete.")
        return redirect(reverse('home'))  # Adjust 'home' to your home page URL name

    return render(request, 'users/profile.html', context)