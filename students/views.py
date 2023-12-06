from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *

# Create your views here.

class StudentDetailAPIView(APIView):
    def get(self, request, *args, **kwargs):
        task_object = Student.objects.get(pk=kwargs.get("pk"))
        serializer = StudentsSerializer(instance=task_object)
        return Response(serializer.data)