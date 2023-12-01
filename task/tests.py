from django.test import TestCase
from django.urls import reverse_lazy
from task.models.task import Task
from django.contrib.auth.models import User

# Create your tests here.

class TaskTestCase(TestCase):
    def test_get_users_list_should_success(self):
        response = self.client.get(reverse_lazy("task:list"))
        self.assertEqual(response.status_code, 200)

class TestTaskDetail(TestCase):
    def test_task_detail_should_success(self):
        user_object = User.objects.create(
            username= 'test_user_1',
            password="bar"
        )
        task_object = Task.objects.create(
            name="task 1",
            description = "wqdqw",
            difficulty = 1,
            created_by = user_object
        )
        print(f"{task_object.name}|{task_object.description}|{task_object.difficulty}|{task_object.created_by}")
        response = self.client.get(f'/api/task/detail/{task_object.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, task_object.name)