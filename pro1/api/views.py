from django.shortcuts import render
from . import models
from . import serializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

def studentDetail(request, pk):
    stu = models.Student.objects.get(id=pk)
    serializer = serializers.StudentSerializer(stu, many=False)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data)

def studentList(request):
    query_Set = models.Student.objects.all()
    serializer = serializers.StudentSerializer(query_Set, many=True)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data, safe=False)