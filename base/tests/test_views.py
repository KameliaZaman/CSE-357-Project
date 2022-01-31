from turtle import circle
from django.http import response
from django.test import TestCase, Client, client
from django.urls import reverse
from base.models import *
import json

class TestViews(TestCase):
    """
	View testing inherited from TestCase class
	"""

    def setUp(self):
        """
        Set up views testing method

        Parameters:
            self: Passes a class related to TestCase
        
        Returns:
            none
        """
        self.client=Client()
        #self.home_url=reverse('home')
        #self.userPage_url=reverse('user-page')
        #self.user_url=reverse('user',args=['Tom'])
        #self.submissionView_url=reverse('submissionView')

    #def test_registerPage_POST(self):
        #url=reverse('register')


    #def test_loginPage_POST(self):


    #def test_logoutUser_POST(self):


    #def test_home_GET(self):
        #response=self.client.get(self.home_url)

        #self.assertEquals(response.status_code,200)
        #self.assertTemplateUsed(response,'accounts/dashboard.html')

    #def test_userPage_GET(self):
        #response=self.client.get(self.userPage_url)

        #self.assertEquals(response.status_code,200)
        #self.assertTemplateUsed(response,'accounts/user.html')

    #def test_profileView_GET(self):
        #response=self.client.get(self.user_url)

        #self.assertEquals(response.status_code,200)
        #self.assertTemplateUsed(response,'accounts/profile.html')

    #def test_submissionViewPage_GET(self):
        #response=self.client.get(self.submissionView_url)

        #self.assertEquals(response.status_code,200)
        #self.assertTemplateUsed(response,'accounts/submissionView.html')

    #def test_uploadCode_POST(self):


    #def test_runCode_POST(self):
