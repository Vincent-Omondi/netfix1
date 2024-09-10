# services/views.py

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from users.models import Company, Customer, User

from .models import Service
from .forms import CreateNewService


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
