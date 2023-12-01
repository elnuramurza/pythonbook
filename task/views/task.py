from rest_framework.views import APIView
from rest_framework.response import Response
from task.models import Task
from task.serializers import TaskSerializer


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