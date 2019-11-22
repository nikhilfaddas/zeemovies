from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Movies,User
from .serializers import MovieSerializer, UserSerializer


# Create your views here
# ViewSets define the view behavior

class MoviesViewSet(ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


