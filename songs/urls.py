from django.urls import path
from .views import *


urlpatterns=[
    path('retrieve_song/<int:pk>/',RetrieveSong.as_view()),
    path('list_song/',ListSong.as_view()),
    path('delete_song/',DeleteSong.as_view()),
    path('update_song/',UpdateSong.as_view()),
    path('post_song/',PostSong.as_view())
]