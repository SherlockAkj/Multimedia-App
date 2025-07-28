from django.db import models

# multimedia_app/models.py
from django.db import models

class Image(models.Model):
    """
    Model to store image files and their metadata.
    """
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    # Stores the image file. 'upload_to' specifies a subdirectory within MEDIA_ROOT.
    file = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Images"
        ordering = ['-uploaded_at'] # Order by most recently uploaded

class Audio(models.Model):
    """
    Model to store audio files and their metadata.
    """
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    # Stores the audio file. 'upload_to' specifies a subdirectory within MEDIA_ROOT.
    file = models.FileField(upload_to='audio/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Audio Tracks"
        ordering = ['-uploaded_at'] # Order by most recently uploaded

class Video(models.Model):
    """
    Model to store video files and their metadata.
    """
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    # Stores the video file. 'upload_to' specifies a subdirectory within MEDIA_ROOT.
    file = models.FileField(upload_to='videos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Videos"
        ordering = ['-uploaded_at'] # Order by most recently uploaded