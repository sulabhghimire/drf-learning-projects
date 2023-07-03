from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api.serializers import StudentSerializer
from api.models import Student

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def studentapi(request, pk=None):

    if request.method == 'GET':
        # id = request.data.get('id')
        id = pk
        
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu, many=False)
        else:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':

        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'PUT':

        # id = request.data.get('id')
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'PATCH':

        # id = request.data.get('id')
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':

        # id = request.data.get('id')
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        
        return Response({'msg' : f'Data with index {id} is deleted.'}, status=status.HTTP_200_OK)


# @api_view(['GET', 'POST'])
# def hello_world(request):

#     if request.method == 'GET':
#         return Response({'msg': 'This is get request'})
    
#     if request.method == 'POST':
#         data = request.data
#         print(data)
#         return Response({'msg': 'This is post request', 'data':request.data})