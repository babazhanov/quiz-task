from django.test import TestCase
from django.test import Client


class SimpleTestCase(TestCase):

    def test_home(self):
        c = Client()
        resp = c.get('/')
        self.assertEqual(resp.status_code, 200)