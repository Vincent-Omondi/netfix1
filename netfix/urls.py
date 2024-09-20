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


handler400 = lambda request, exception=None: error_view(request, exception, status=400)
handler403 = lambda request, exception=None: error_view(request, exception, status=403)
handler404 = lambda request, exception=None: error_view(request, exception, status=404)
handler500 = lambda request: error_view(request, status=500)