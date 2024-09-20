# netfix/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler400, handler403, handler404, handler500
from main.views import error_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),  # Include users app URLs
    path('services/', include('services.urls')),  # Include services app URLs
    path('', include('main.urls')),  # Include main app URLs
]

handler400 = error_view
handler403 = error_view
handler404 = error_view
handler500 = error_view