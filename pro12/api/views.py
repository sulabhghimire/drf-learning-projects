from api import models
from api import serializers

from rest_framework import viewsets

class StudentModelViewSet(viewsets.ModelViewSet):

    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer

class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer