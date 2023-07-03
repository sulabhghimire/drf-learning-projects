from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from api.models import Student
from api.serializers import StudentSerializer

from rest_framework.generics import ListAPIView

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['city', 'pass_by']
    search_fields = ['name']
    ordering_fields = ['name',  'city', 'roll']
    # search_fields = ['pass_by', 'name']