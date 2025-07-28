# multimedia_app/views.py
from django.shortcuts import render
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

