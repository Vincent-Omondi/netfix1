# services/models.py
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from users.models import Company, Customer

class Service(models.Model):
    """
    Model representing a service offered by a company.
    """
    # Service fields
    name = models.CharField(max_length=40)
    description = models.TextField()
    price_hour = models.DecimalField(decimal_places=2, max_digits=100)
    date = models.DateTimeField(auto_now=True, null=False)

    # Service category choices
    CATEGORY_CHOICES = (
        ('Air Conditioner', 'Air Conditioner'),
        ('Carpentry', 'Carpentry'),
        ('Electricity', 'Electricity'),
        ('Gardening', 'Gardening'),
        ('Home Machines', 'Home Machines'),
        ('House Keeping', 'House Keeping'),
        ('Interior Design', 'Interior Design'),
        ('Locks', 'Locks'),
        ('Painting', 'Painting'),
        ('Plumbing', 'Plumbing'),
        ('Water Heaters', 'Water Heaters'),
    )
    field = models.CharField(max_length=30, blank=False, null=False, choices=CATEGORY_CHOICES)

    # Relationships
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    # Rating field with validation
    rating = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        null=True,
        default=None
    )

    def __str__(self):
        """String representation of the Service."""
        return self.name

class ServiceHistory(models.Model):
    """
    Model representing the history of service requests.
    """
    # Service request details
    price = models.DecimalField(decimal_places=2, max_digits=10)
    request_date = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=200)
    service_time = models.IntegerField()

    # Relationships
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    # Rating field with validation
    rating = models.FloatField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        null=True,
        blank=True
    )

    def __str__(self):
        """String representation of the ServiceHistory."""
        return f"{self.customer.user.username} - {self.service.name}"