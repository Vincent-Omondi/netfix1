# users/views.py

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

def loginUserView(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            try:
                user = User.objects.get(email=email)

                user = authenticate(request, username=user.username, password=user.password)
                if user is not None:
                    login(request, user)
                    return redirect('user/profile.html')
                else:

                    form.add_error(None, "Invalid credentials.")
            except User.DoesNotExist:
                form.add_error(None, "User Does Not Exist")
        else:
            form = UserLoginForm()
        return render(request, 'users/login.html', {'form': form})

