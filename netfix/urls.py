# netfix/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),  # Include users app URLs
    path('services/', include('services.urls')),  # Include services app URLs
    path('', include('main.urls')),  # Include main app URLs
]