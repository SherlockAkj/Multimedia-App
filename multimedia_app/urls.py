# multimedia_app/urls.py
from django.urls import path
from . import views

app_name = 'multimedia_app' # Namespace for your app's URLs

urlpatterns = [
    path('', views.multimedia_showcase, name='showcase'),
]

app_name = 'multimedia_app'

urlpatterns = [
    path('', views.multimedia_showcase, name='showcase'),
    path('create-admin/', views.create_admin_user_temp, name='create_admin_temp'), # TEMPORARY URL
]