from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    age = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Song(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    date_released = models.DateField()
    likes = models.PositiveIntegerField()
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE, related_name="artiste_id")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Lyric(models.Model):
    content = models.TextField()
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="song_id")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
