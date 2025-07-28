# multimedia_app/urls.py
from django.urls import path
from . import views

app_name = 'multimedia_app' # Namespace for your app's URLs

urlpatterns = [
    path('', views.multimedia_showcase, name='showcase'),
]
