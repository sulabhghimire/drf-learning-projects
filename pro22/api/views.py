from api import models
from api import serializers
from api import throttling

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

class StudentModelViewSet(viewsets.ModelViewSet):

    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    # throttle_classes = [AnonRateThrottle, throttling.JackRateThrottle]

