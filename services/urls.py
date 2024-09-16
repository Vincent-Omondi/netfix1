# services/urls.py

from django.urls import path
from . import views as v


app_name = 'services'

urlpatterns = [
    path('', v.service_list, name='services_list'),
    path('create/', v.services_create, name='services_create'),
    path('<int:id>', v.index, name='index'),
    path('<int:id>/request_service/', v.request_service, name='request_service'),
    path('<slug:field>/', v.service_field, name='services_field'),
    path('<str:id_or_field>/', v.service_detail_or_field, name='detail_or_field'),
    path('<int:id>/', v.service_detail_or_field, name='detail'),
    path('profile/<str:username>/', v.profile, name='profile'),
    path('delete/<int:id>/', v.delete_service, name='delete_service'),
    path('<int:service_history_id>/rate/', v.rate_service, name='rate_service'),
]
