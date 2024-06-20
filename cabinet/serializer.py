from .models import UserCabinet
from rest_framework.serializers import ModelSerializer

class UserCabinetSerializer(ModelSerializer):
    class Meta:
        model=UserCabinet
        fields='__all__'