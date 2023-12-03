from rest_framework.views import APIView
from rest_framework.response import Response
from task.models.task import *
from task.serializers.task import *


class TaskDetailAPIView(APIView):
    def get(self, request, *args, **kwargs):
        task_object = Task.objects.get(pk=kwargs.get("pk"))
        serializer = TaskSerializer(instance=task_object)
        return Response(serializer.data)
    
class TasksView(APIView):
    def get(self, request, *args, **kwargs):
        task_list = Task.objects.all()
        serializer = TaskSerializer(task_list, many=True)
        # json_data = user_serializer.data
        return Response(serializer.data)
    
class AnswersView(APIView):
    def get(self, request, *args, **kwargs):
        answer_list = Answer.objects.all()
        serializer = AnswerSerializer(answer_list, many=True)
        return Response(serializer.data)
    
class AnswerDetailAPIView(APIView):
    def get(self, request, *args, **kwargs):
        answer_object = Answer.objects.get(pk=kwargs.get("pk"))
        serializer = AnswerSerializer(instance=answer_object)
        return Response(serializer.data)
    