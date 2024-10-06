# users/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import User, Company, Customer
from django.utils import timezone
from datetime import timedelta

# Custom widget for date input
class DateInput(forms.DateInput):
    input_type = 'date'

# Custom email validation function
def validate_email(value):
    """
    Validate that the email is not already in use.
    """
    if User.objects.filter(email=value).exists():
        raise ValidationError(f"{value} is already taken.")

# Base form for user creation
class BaseUserCreationForm(UserCreationForm):
    email = forms.EmailField(validators=[validate_email])

    class Meta:
        model = User
        fields = ("username", "email")

# Form for customer sign up
class CustomerSignUpForm(BaseUserCreationForm):
    birth = forms.DateField(
        label="Date of Birth",
        widget=DateInput(attrs={'type': 'date'}),
    )

    def clean_birth(self):
        birth = self.cleaned_data.get("birth")
        min_age_date = timezone.now().date() - timedelta(days=10 * 365)
        
        if birth and birth > min_age_date:
            raise forms.ValidationError("You must be at least 10 years old.")

        return birth

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_customer = True
        if commit:
            user.save()
            if self.cleaned_data.get("birth"):
                Customer.objects.create(user=user, birth=self.cleaned_data["birth"])
        return user

# Form for company sign up
class CompanySignUpForm(BaseUserCreationForm):
    field_of_work_choices = [
        ('Air Conditioner', 'Air Conditioner'),
        ('All in One', 'All in One'),
        ('Carpentry', 'Carpentry'),
        ('Electricity', 'Electricity'),
        ('Gardening', 'Gardening'),
        ('Home Machines', 'Home Machines'),
        ('House keeping', 'House keeping'),
        ('Interior Design', 'Interior Design'),
        ('Locks', 'Locks'),
        ('Painting', 'Painting'),
        ('Plumbing', 'Plumbing'),
        ('Water Heaters', 'Water Heaters'),
    ]
    field_of_work = forms.ChoiceField(
        choices=field_of_work_choices,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_company = True
        if commit:
            user.save()
            if self.cleaned_data.get("field_of_work"):
                Company.objects.create(user=user, field=self.cleaned_data["field_of_work"])
        return user

# Form for user login
class UserLoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Email',
            'autocomplete': 'off'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Password'
        })
    )

    def clean(self):
        """
        Custom clean method to authenticate the user.
        """
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            user = User.objects.filter(email=email).first()
            if user and user.check_password(password):
                if not user.is_active:
                    raise forms.ValidationError("This account is inactive.")
            else:
                raise forms.ValidationError("Invalid email or password.")

        return cleaned_data

    def get_user(self):
        """
        Return the authenticated user.
        """
        email = self.cleaned_data.get('email')
        return User.objects.filter(email=email).first()