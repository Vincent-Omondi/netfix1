# main/views.py
from django.shortcuts import render
from django.contrib.auth import logout as django_logout
from django.db.models import Count
from services.models import Service, ServiceHistory


def logout(request):
    # Log out the user using Django's built-in logout function
    django_logout(request)
    # Render the logout page
    return render(request, "main/logout.html")


def home(request):
    # Query for the 8 most requested services
    most_requested_services = Service.objects.annotate(
        request_count = Count('servicehistory')
    ).filter(request_count__gt=0).order_by('-request_count')[:8]

    # Prepare the context dictionary for the template
    context = {
        'most_requested_services': most_requested_services,
    }
    # Render the home page with the context
    return render(request, "main/home.html", context)
    
def error_view(request, exception=None, status=None):
    # Handle error pages with a custom template
    # Use the status code passed by Django (if it's provided)
    status_code = status if status else 500
    # Render the error template with the status code
    return render(request, 'error.html', {'code': status_code}, status=status_code)