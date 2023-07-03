from django.shortcuts import render

from api.serializers import SingerSerializers, SongSerializers
from api.models import Singer, Song

from rest_framework import viewsets

class SingerViewSet(viewsets.ModelViewSet):

    queryset = Singer.objects.all()
    serializer_class = SingerSerializers

class SongViewSet(viewsets.ModelViewSet):

    queryset = Song.objects.all()
    serializer_class = SongSerializers