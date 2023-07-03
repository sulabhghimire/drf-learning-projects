from api import models
from api import serializers

from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication

from api import custompermissions

class StudentModelViewSet(viewsets.ModelViewSet):

    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes=[custompermissions.MyPermission]
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    # permission_classes = [DjangoModelPermissions]
    # permission_classes = [IsAdminUser]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]