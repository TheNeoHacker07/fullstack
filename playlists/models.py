from django.db import models 
from django.contrib.auth import get_user_model
from songs.models import SongModel
from django.utils.text import slugify


User = get_user_model()

class Playlist(models.Model):
    author = models.ForeignKey(User, related_name='playlist', on_delete=models.CASCADE,blank=True, verbose_name='автор')
    name = models.CharField(max_length=25)
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    songs = models.ManyToManyField(SongModel,blank=True, related_name='playlists')

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.name)

        super().save(*args,**kwargs)

    def __str__(self):
        return self.name

