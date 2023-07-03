from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from api.serializers import StudentSerializer
from api.models import Student

class StudentAPI(APIView):

    def get(self, request, pk=None, format=None):
        id = pk
        
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu, many=False)
        else:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format = None):
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk, format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, pk, format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        
        return Response({'msg' : f'Data with index {id} is deleted.'}, status=status.HTTP_200_OK)
