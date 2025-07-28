# multimedia_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings # Import settings
from django.conf.urls.static import static # Import static helper

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('multimedia_app.urls')), # Include your app's URLs
]

# ONLY add this to serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Optional: Also serve static files in development if not using collectstatic
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)