from django.shortcuts import render
from django.contrib.auth import logout as django_logout
from django.db.models import Count
from services.models import Service, ServiceHistory


def home(request):
    return render(request, "main/home.html", {})


def logout(request):
    django_logout(request)
    return render(request, "main/logout.html")


def home(request):
    most_requested_services = Service.objects.annotate(
        request_count = Count('servicehistory')
    ).filter(request_count__gt=0).order_by('-request_count')[:8]

    context = {
        'most_requested_services': most_requested_services,
    }
    return render(request, "main/home.html", context)
    