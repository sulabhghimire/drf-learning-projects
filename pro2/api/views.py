from django.shortcuts import render
from .serializers import StudentSerializer
import io
from rest_framework.parsers import JSONParser 
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def student_create(request):
    if request.method=='POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)

        if serializer.is_valid():
            serializer.save()
            message = {'msg' : 'Data Created'}
            json_data = JSONRenderer().render(message)
            return HttpResponse(json_data, content_type='application/json')
        else:
            message = {'msg' : serializer.errors}
            json_data = JSONRenderer().render(message)
            return HttpResponse(json_data, content_type='application/json')
    
    else:
        message = {'msg' : 'Not a post request'}
        json_data = JSONRenderer().render(message)
        return HttpResponse(json_data, content_type='application/json')




# Create your views here.
