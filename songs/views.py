from django.shortcuts import render

from rest_framework.generics import ListAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView,CreateAPIView
from rest_framework.permissions import AllowAny,IsAuthenticated


from .models import SongModel
from .serializers import SongSerializers


from .permissions import IsOwnerOrReadOnly
from rest_framework import filters

from django_filters.rest_framework import DjangoFilterBackend

class ListSong(ListAPIView):
    queryset=SongModel.objects.all()
    serializer_class=SongSerializers
    filter_backends=[filters.SearchFilter,DjangoFilterBackend]
    filterset_fields=['author']
    search_fields=['title','genre']
    
class RetrieveSong(RetrieveAPIView):
    queryset=SongModel.objects.all()
    serializer_class=SongSerializers
    lookup_field='pk'
    filter_backends=[filters.SearchFilter,DjangoFilterBackend]
    filterset_fields=['author']
    search_fields=['title','genre']


class DeleteSong(DestroyAPIView):
    queryset=SongModel.objects.all()
    serializer_class=SongSerializers
    lookup_field='pk'
    permission_classes=[IsAuthenticated,IsOwnerOrReadOnly]


class UpdateSong(UpdateAPIView):
    queryset=SongModel.objects.all()
    serializer_class=SongSerializers
    lookup_field='pk'
    permission_classes=[IsAuthenticated,IsOwnerOrReadOnly]    
    


class PostSong(CreateAPIView):
    queryset=SongModel.objects.all()
    serializer_class=SongSerializers
    permission_classes=[IsAuthenticated] 




# Create your views here.
