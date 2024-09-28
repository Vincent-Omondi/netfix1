# services/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.db.models import Avg, Count
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from users.models import Company, Customer, User
from .models import Service, ServiceHistory
from .forms import CreateNewService, RequestServiceForm

# List all services
def service_list(request):
    sort_by = request.GET.get('sort_by', 'date')  # Default sorting by date

    if sort_by == 'requests':
        # Sort by most requested services (counting ServiceHistory records)
        services = Service.objects.annotate(request_count=Count('servicehistory')).order_by('-request_count')
    else:
        # Sort by creation date (default)
        services = Service.objects.all().order_by('-date')

    return render(request, 'services/list.html', {'services': services, 'sort_by': sort_by})

# Display service detail or field
def service_detail_or_field(request, id_or_field):
    try:
        # Try to get a service by id
        service = get_object_or_404(Service, id=int(id_or_field))
        return render(request, 'services/fields.html', {'services': [service], 'field': service.field})
    except ValueError:
        # If id_or_field is not an integer, treat it as a field
        return service_field(request, id_or_field)

# Display single service
def index(request, id):
    service = Service.objects.get(id=id)
    
    # Fetch the service history for the logged-in customer if available
    service_history = None
    if request.user.is_authenticated and hasattr(request.user, 'customer'):
        service_history = ServiceHistory.objects.filter(service=service, customer=request.user.customer).first()

    return render(request, 'services/single_service.html', {
        'service': service,
        'service_history': service_history,
    })

# Create a new service
@login_required
def services_create(request):
    if request.method == 'POST':
        form = CreateNewService(request.POST, company=request.user.company)
        if form.is_valid():
            service = form.save(commit=False)
            service.company = request.user.company
            service.save()
            return redirect('services:index', id=service.id)
    else:
        form = CreateNewService(company=request.user.company)
    
    return render(request, 'services/create.html', {'form': form})

# Request a service
@login_required
def request_service(request, id):
    service = get_object_or_404(Service, id=id)
    if request.method == 'POST':
        form = RequestServiceForm(request.POST)
        if form.is_valid():
            service_history = form.save(commit=False)
            service_history.service = service
            service_history.customer = request.user.customer
            service_history.price = service.price_hour * form.cleaned_data['service_time']
            service_history.save()
            return redirect('users:profile', username=request.user.username)
    else:
        form = RequestServiceForm()
    
    return render(request, 'services/request_service.html', {'form': form, 'service': service})

# Display user profile
def profile(request, username):
    # TODO: Implement profile view
    pass

# Display services by field
def service_field(request, field):
    field = field.replace('-', ' ').title()
    sort_by = request.GET.get('sort_by', 'date')  # Default sorting by date

    if sort_by == 'requests':
        # Sort by most requested services (counting ServiceHistory records)
        services = Service.objects.filter(field=field).annotate(request_count=Count('servicehistory')).order_by('-request_count')
    else:
        # Sort by creation date (default)
        services = Service.objects.filter(field=field).order_by('-date')

    return render(request, 'services/field.html', {'services': services, 'field': field, 'sort_by': sort_by})

# Delete a service
@login_required
def delete_service(request, id):
    service = get_object_or_404(Service, id=id)
    
    # Check if the current user is the owner of the service
    if request.user.company == service.company:
        service.delete()
        messages.success(request, 'Service deleted successfully.')
    else:
        messages.error(request, 'You do not have permission to delete this service.')
    
    return redirect('users:profile', username=request.user.username)

# Rate a service
@login_required
@require_POST
def rate_service(request, service_history_id):
    service_history = get_object_or_404(ServiceHistory, id=service_history_id, customer=request.user.customer)
    
    try:
        rating = float(request.POST.get('rating', 0))
        if not (1 <= rating <= 5):
            raise ValidationError('Rating must be between 1 and 5.')
    except (ValueError, ValidationError):
        return JsonResponse({
            'success': False,
            'error': 'Invalid rating value. Please provide a number between 1 and 5.'
        })
    
    service_history.rating = rating
    service_history.save()
    
    # Calculate the new average rating
    average_rating = ServiceHistory.objects.filter(
        service=service_history.service, 
        rating__isnull=False
    ).aggregate(Avg('rating'))['rating__avg']
    
    # Update the service's rating
    if average_rating is not None:
        service_history.service.rating = round(average_rating, 1)
        service_history.service.save()
    
    return JsonResponse({
        'success': True,
        'message': 'Rating updated successfully.',
        'new_rating': rating,
        'new_average_rating': service_history.service.rating
    })