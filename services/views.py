# services/views.py

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from users.models import Company, Customer, User

from .models import Service, ServiceHistory
from .forms import CreateNewService, RequestServiceForm


def service_list(request):
    services = Service.objects.all().order_by("-date")
    return render(request, 'services/list.html', {'services': services})

def service_detail_or_field(request, id_or_field):
    try:
        # Try to get a service by id
        service = get_object_or_404(Service, id=int(id_or_field))
        return render(request, 'services/fields.html', {'services': [service], 'field': service.field})
    except ValueError:
        # If id_or_field is not an integer, treat it as a field
        return service_field(request, id_or_field)

def index(request, id):
    service = Service.objects.get(id=id)
    return render(request, 'services/single_service.html', {'service': service})



@login_required
def services_create(request):
    # if not hasattr(request.user, 'company'):
    #     return redirect('/')
    
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



def service_field(request, field):
    # search for the service present in the url
    field = field.replace('-', ' ').title()
    services = Service.objects.filter(
        field=field)
    return render(request, 'services/field.html', {'services': services, 'field': field})


def request_service(request, id):
    return render(request, 'services/request_service.html', {})


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

def profile(request, uername):

    pass

from django.db.models import Count

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

