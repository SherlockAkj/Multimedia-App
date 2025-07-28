from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User # Import User model
from .models import Image, Audio, Video

def multimedia_showcase(request):
    """
    View to display all multimedia content (images, audio, videos).
    Fetches all objects from their respective models and passes them to the template.
    """
    images = Image.objects.all()
    audio_tracks = Audio.objects.all()
    videos = Video.objects.all()

    context = {
        'images': images,
        'audio_tracks': audio_tracks,
        'videos': videos,
    }
    return render(request, 'multimedia_app/multimedia_showcase.html', context)

# multimedia_app/views.py
def multimedia_showcase(request):
    # ... (your existing code for multimedia_showcase) ...
    images = Image.objects.all()
    audio_tracks = Audio.objects.all()
    videos = Video.objects.all()

    context = {
        'images': images,
        'audio_tracks': audio_tracks,
        'videos': videos,
    }
    return render(request, 'multimedia_app/multimedia_showcase.html', context)

def create_admin_user_temp(request):
    # IMPORTANT: Remove this view immediately after use for security!
    # Choose a unique username and a strong password here
    admin_username = 'your_admin_username' # <--- CHANGE THIS
    admin_email = 'admin@example.com'      # <--- CHANGE THIS (optional, but good practice)
    admin_password = 'your_strong_password' # <--- CHANGE THIS TO A REAL STRONG PASSWORD

    if not User.objects.filter(username=admin_username).exists():
        User.objects.create_superuser(admin_username, admin_email, admin_password)
        return HttpResponse(f"Admin user '{admin_username}' created successfully. **DELETE THIS VIEW NOW!**")
    return HttpResponse(f"Admin user '{admin_username}' already exists or creation failed.")