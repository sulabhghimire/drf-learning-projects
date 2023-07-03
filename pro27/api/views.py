from api.models import Student
from api.serializers import StudentSerializer
from api.pagination import MyOffsetPagination

from rest_framework.generics import ListAPIView

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyOffsetPagination
