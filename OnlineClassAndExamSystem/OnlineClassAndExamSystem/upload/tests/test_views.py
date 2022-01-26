from http import client
from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from upload.models import questionAndSolution
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url= reverse('home')
        self.show_url = reverse('show')

    def test_home_GET(self):

        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'home.html')

    def test_show_GET(self):

        response =self.client.get(self.show_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'quesAndSolveList.html')