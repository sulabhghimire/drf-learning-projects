from api import models
from api import serializers

from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly

class StudentModelViewSet(viewsets.ModelViewSet):

    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    # permission_classes = [DjangoModelPermissions]
    # permission_classes = [IsAdminUser]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]