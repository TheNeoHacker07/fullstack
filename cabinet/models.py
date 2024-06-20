from django.db import models
from django.contrib.auth import get_user_model
from songs.models import SongGenre 

# Create your models here.

User=get_user_model()

class UserCabinet(models.Model):
    author=models.ForeignKey(User,related_name='user_cabinet',on_delete=models.CASCADE,verbose_name='пользаватель')
    nickname=models.CharField(max_length=100,verbose_name='имя')
    about_user=models.CharField(max_length=123,verbose_name='О себе')
    favorite_genres=models.ForeignKey(SongGenre,on_delete=models.SET_NULL,null=True,verbose_name='любимый жанр')
    user_image=models.ImageField(upload_to='user/img/',verbose_name='фото пользавателя',blank=True)
    image=models.ImageField(upload_to='banner/img/',verbose_name='фото баннера',blank=True)



    def __str__(self) -> str:
        return self.nickname




