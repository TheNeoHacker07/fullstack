from django.urls import path

from .views import *

urlpatterns = [
    path('playlists/', PlaylistListView.as_view()),
    path('playlist/<slug:slug>/', PlaylistDetail.as_view()),
    path('playlist_delete/<slug:slug>/',PlaylistDelete.as_view()),
    path('playlist_create/',PlayListCreate.as_view())
]
