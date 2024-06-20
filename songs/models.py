from django.db import models
from django.contrib.auth import get_user_model


User=get_user_model()

class SongGenre(models.Model):
    song_genre=models.CharField(max_length=12,verbose_name='ЖАНР')

    def __str__(self):
        return self.song_genre







class SongModel(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='songs')
    genre=models.ForeignKey(SongGenre,on_delete=models.SET_NULL,null=True,related_name='genre')
    song_name=models.CharField(max_length=30,verbose_name='название')
    description=models.CharField(max_length=100,verbose_name='описание')
    song_text=models.CharField(max_length=25000 ,verbose_name='текст песни')
    song_image=models.ImageField(upload_to='songs/image/',blank=True,verbose_name='картинка песни')
    song=models.FileField(upload_to='songs/audio/',blank=True)

    # created_at=models.DateTimeField(auto_now_add=True)
    # updated_at=models.DateField(auto_now=True)


    def __str__(self):
        return self.song_name
    










# Create your models here.
