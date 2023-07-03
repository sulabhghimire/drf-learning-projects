from django.shortcuts import render

from api.serializers import StudentSerializers
from api.models import Student

from rest_framework import viewsets

class StudentViewSer(viewsets.ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializers
