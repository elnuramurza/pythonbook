from django.urls import path
from task.views.task import *

app_name = 'task'

urlpatterns = [
    path('detail/<int:pk>/', TaskDetailAPIView.as_view(), name="task-detail"),
    path('list/', TasksView.as_view(), name='list'),
    # path('detail/<int:pk>/', AnswerDetailAPIView.as_view(), name="answer-detail"),
    # path('list/', AnswersView.as_view(), name='list'),
]