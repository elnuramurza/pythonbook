from django.test import TestCase
from django.urls import reverse_lazy
from task.models.task import *
from django.contrib.auth.models import User

# Create your tests here.

class TaskTestCase(TestCase):
    def test_get_users_list_should_success(self):
        response = self.client.get(reverse_lazy("task:list"))
        self.assertEqual(response.status_code, 200)

class TestTaskDetail(TestCase):
    def test_task_detail_should_success(self):
        task_object = Task.objects.create(
            name="task_1",
            description = "wqdqw",
            difficulty = 1,
            created_by = Mentor.objects.create(
                user = User.objects.create(
                    username= 'test_user_1',
                    password="qwqewrtert"),
                name = 'mentor1'
            ))
        print(f"{task_object.name}|{task_object.description}|{task_object.difficulty}|{task_object.created_by}")
        response = self.client.get(f'/api/task/detail/{task_object.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, task_object.name)

class AnswerTestCase(TestCase):
    def test_get_answer_list_should_success(self):
        response = self.client.get(reverse_lazy("answer:list"))
        self.assertEqual(response.status_code, 200)

class TestAnswerDetail(TestCase):
    def test_answer_detail_should_success(self):
        answer_object = Answer.objects.create(
            txt="answer_test_1",
            profile = Profile.objects.create(
                user = User.objects.create(
                    username= 'test_user_2',
                    password="qwerty"
                ),
                name = 'profile1'),
            task= Task.objects.create(
                name="task_2",
                description = "wqdqw",
                difficulty = 2,
                created_by = Mentor.objects.create(
                    user = User.objects.create(
                        username= 'test_user_3',
                        password="qweertasd"),
                    name = 'mentor2'
            )))
        print(answer_object.txt)
        response = self.client.get(f'/api/answer/detail/{answer_object.id}/')
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, answer_object.txt)