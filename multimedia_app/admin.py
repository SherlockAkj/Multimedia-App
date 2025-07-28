# multimedia_app/admin.py
from django.contrib import admin
from .models import Image, Audio, Video

# Register your models here.
admin.site.register(Image)
admin.site.register(Audio)
admin.site.register(Video)
