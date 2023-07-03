from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from api.models import Student
from api.serializers import StudentSerializers

@method_decorator(csrf_exempt, name='dispatch')
class StudentApi(View):

    def get(self, request, *args, **kwargs):
        data = request.body
        stream = io.BytesIO(data)
        python_data = JSONParser().parse(stream)

        id = python_data.get('id', None)

        if id is not None:

            try:
                stu = get_object_or_404(Student, id=id)
                serializer = StudentSerializers(stu, many=False)
                json_data = JSONRenderer().render(serializer.data)
            
            except Http404:
                error_data = {'err_msg': f'Record doesn\'t exists at {id}.'}
                json_data = JSONRenderer().render(error_data)

        else:
            stu = Student.objects.all()
            serializer = serializer = StudentSerializers(stu, many=True)
            json_data = JSONRenderer().render(serializer.data)

        return HttpResponse(json_data, content_type='application/json')
    
    
    def post(self, request, *args, **kwargs):

        data = request.body
        stream = io.BytesIO(data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializers(data = python_data)

        if serializer.is_valid():
            serializer.save()
            res = {'msg' : 'Data inserted'}
            json_data = JSONRenderer().render(res)
        
        else:
            json_data = JSONRenderer().render(serializer.errors)

        return HttpResponse(json_data, content_type='application/json')


    def put(self, request, *args, **kwargs):

        data = request.body
        stream = io.BytesIO(data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')

        try:
            stu = get_object_or_404(Student, id=id)
            serializer = StudentSerializers(stu, data=python_data, partial=True)

            if serializer.is_valid():
                serializer.save()
                res = {'msg' : 'Data updates'}
                json_data = JSONRenderer().render(res)
            
            else:
                json_data = JSONRenderer().render(serializer.errors)

        except:
            error_data = {'err_msg': f'Record doesn\'t exists at {id} so can\'t be updated.'}
            json_data = JSONRenderer().render(error_data)

        return HttpResponse(json_data, content_type='application/json')
    

    def delete(self, request, *args, **kwargs):

        data = request.body
        stream = io.BytesIO(data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')

        try:
            stu = Student.objects.get(id=id)
            stu.delete()
            msg = {'msg' : f'Record at id {id} is deleted.'}
            json_data = JSONRenderer().render(msg)

        except:
            error_data = {'err_msg' : f'Record doesn\'t exists at {id} so can\'t be deleted.'}
            json_data = JSONRenderer().render(error_data)

        return HttpResponse(json_data, content_type='application/json')