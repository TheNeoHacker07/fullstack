from .models import SongModel,SongGenre
from rest_framework import serializers


class SongSerializers(serializers.ModelSerializer):
    
    class Meta:
        model=SongModel
        fields='__all__'

    def create(self, validated_data):
        validated_data['author']=self.context['request'].user
        post=super().create(validated_data)
        post.save()
        return post
    


class SongGengreSerializer(serializers.ModelSerializer):
    class Meta:
        model=SongGenre
        fields='__all__'