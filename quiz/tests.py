from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient


class AvailableTestCase(TestCase):

    def test_home(self):
        client = APIClient()
        resp = client.get('/')
        self.assertEqual(resp.status_code, 200)
        return client


class APITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.my_admin = User(username='admin')
        self.my_admin.is_staff = True
        self.my_admin.is_admin = True
        self.my_admin.is_superuser = True
        self.my_admin.set_password('admin')
        self.my_admin.save()

        login_response = self.client.login(username='admin', password='admin')
        self.assertTrue(login_response)

    def add_quiz(self):
        resp = self.client.post('/quizzes/', {
            'title': 'title',
            'date_start': '2020-08-01',
            'date_end': '2020-08-30',
            'description': 'description'
        }, format='json')
        self.assertEqual(resp.status_code, 201)

    def get_quizzes(self):
        resp = self.client.get('/quizzes/', format='json')
        self.assertEqual(resp.status_code, 200)

    def add_simple(self):
        print(reverse('quiz-detail', kwargs={"pk": 1}))
        resp = self.client.post('/simple/', {
            'quiz': reverse('quiz-detail', kwargs={"pk": 1}),
            'question': 'Кто проживает на дне океана?'
        }, format='json')
        self.assertEqual(resp.status_code, 201)

    def get_simple(self):
        resp = self.client.get('/simple/', format='json')
        self.assertEqual(resp.status_code, 200)

    def test_sequence(self):
        self.add_quiz()
        self.get_quizzes()
        self.add_simple()
        self.get_simple()
