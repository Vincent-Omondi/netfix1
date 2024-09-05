# users/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

class User(AbstractUser):
    is_company = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    email = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=100, unique=True)

    # Override groups and user_permissions to avoid reverse accessor clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',  # Unique related name
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions '
                  'granted to each of their groups.',
        verbose_name='groups'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # Unique related name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    birth = models.DateField()

    def __str__(self):
        return str(self.user.id) + ' - ' + self.user.username

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    field = models.CharField(max_length=70, choices=[
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
    ], blank=False, null=False)
    rating = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(0)], default=0)

    def __str__(self):
        return str(self.user.id) + ' - ' + self.user.username