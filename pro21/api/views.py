from api import models
from api import serializers

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class StudentModelViewSet(viewsets.ModelViewSet):

    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

# http http://127.0.0.1:8000/studentapi/ 'Authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3NDk5NTExLCJpYXQiOjE2ODc0OTgxMjMsImp0aSI6IjU4YTU1ZThhYWIxNDRjZWZhYjMyMDM2NmJlZjk5ZGM1IiwidXNlcl9pZCI6MX0.-6yO2-amEPjPJ-xaWKc2jHNwvHb0aqBIlb8fOu6ZdgE