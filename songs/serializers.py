from .models import SongModel
from rest_framework import serializers


class SongSerializers(serializers.ModelSerializer):
    class Meta:
        model=SongModel
        fields='__all__'


        