from django.test import TestCase
from django.urls import reverse   # resolve

# from boards.views import home
from boards.models import Board


class HomeTests(TestCase):

    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django board.')
        url = reverse('home')
        self.response = self.client.get(url)

    # A simple test to testing the status code response 200 (success)
    def test_home_view_status_code(self):
        self.assertEqual(self.response.status_code, 200)
