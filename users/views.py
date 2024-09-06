# users/views.py

from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from .forms import CustomerSignUpForm, CompanySignUpForm, UserLoginForm
from .models import User

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
        return redirect('/')

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
        return redirect('/')

@csrf_exempt
def loginUserView(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            try:
                user = User.objects.get(email=email)
                authenticated_user = authenticate(request, username=user.username, password=password)
                if authenticated_user is not None:
                    login(request, authenticated_user)
                    return redirect('user_profile')  # Make sure this URL name is defined in your urls.py
                else:
                    messages.error(request, "Invalid credentials.")
            except User.DoesNotExist:
                messages.error(request, "User does not exist.")
        else:
            messages.error(request, "Form is not valid.")
    else:
        form = UserLoginForm()
    
    return render(request, 'users/login.html', {'form': form})
