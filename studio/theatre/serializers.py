from rest_framework.serializers import ModelSerializer
from .models import Movies,User

# Serializers define the API representation

class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'