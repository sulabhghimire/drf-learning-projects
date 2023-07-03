from api import models
from api import serializers
from api.custauth import CustomAuthentication

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class StudentModelViewSet(viewsets.ModelViewSet):

    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]