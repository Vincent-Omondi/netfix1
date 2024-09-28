# services/urls.py
from django.urls import path
from . import views as v

app_name = 'services'

urlpatterns = [
    # List all services
    path('', v.service_list, name='services_list'),

    # Create a new service
    path('create/', v.services_create, name='services_create'),

    # Service detail views
    path('<int:id>/', v.index, name='index'),
    path('detail/<int:id>/', v.service_detail_or_field, name='detail'),
    path('<str:id_or_field>/', v.service_detail_or_field, name='detail_or_field'),

    # Service field view
    path('field/<slug:field>/', v.service_field, name='services_field'),

    # Service actions
    path('<int:id>/request_service/', v.request_service, name='request_service'),
    path('delete/<int:id>/', v.delete_service, name='delete_service'),
    path('<int:service_history_id>/rate/', v.rate_service, name='rate_service'),

    # I might use this url later
    # path('profile/<str:username>/', v.profile, name='profile'),
]