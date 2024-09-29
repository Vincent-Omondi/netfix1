# users/models.py

# Django imports
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

# Third-party imports
from dateutil.relativedelta import relativedelta

class UserManager(BaseUserManager):
    """Custom user manager to handle email as the unique identifier."""

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular user with the given email and password."""
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a superuser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    """Custom user model using email as the unique identifier."""

    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField('email address', unique=True)
    is_company = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    # Override groups and user_permissions to avoid reverse accessor clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions '
                  'granted to each of their groups.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    def __str__(self):
        return self.username

class Customer(models.Model):
    """Model representing a customer user."""

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    birth = models.DateField()

    def __str__(self):
        return f"{self.user.id} - {self.user.username}"

    def age(self):
        """Calculate the customer's age."""
        today = timezone.now().date()
        return relativedelta(today, self.birth).years

class Company(models.Model):
    """Model representing a company user."""

    FIELD_CHOICES = [
        ('Air Conditioner', 'Air Conditioner'),
        ('All in One', 'All in One'),
        ('Carpentry', 'Carpentry'),
        ('Electricity', 'Electricity'),
        ('Gardening', 'Gardening'),
        ('Home Machines', 'Home Machines'),
        ('House Keeping', 'House Keeping'),
        ('Interior Design', 'Interior Design'),
        ('Locks', 'Locks'),
        ('Painting', 'Painting'),
        ('Plumbing', 'Plumbing'),
        ('Water Heaters', 'Water Heaters')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    field = models.CharField(max_length=70, choices=FIELD_CHOICES, blank=False, null=False)
    rating = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(0)],
        default=0
    )

    def __str__(self):
        return f"{self.user.id} - {self.user.username}"