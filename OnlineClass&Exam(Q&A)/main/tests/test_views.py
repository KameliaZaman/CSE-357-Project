from pydoc import cli
from unittest import TestCase
from django.test import TestCase, Client
from django.urls import reverse
from main.models import questionModel, responseOnQuestion
import json



class testViews(TestCase):
		"""
		This class tests views.py.
		"""

		def setUp(self):
			"""
			This function sets up the client, registerUrl and loginUrl.
			"""
			self.client = Client()
			self.registerUrl = reverse('register')
			self.loginUrl = reverse('login')
			# self.logoutUrl = reverse('logout')

		def testRegisterPagePOST(self):
				"""
				This function tests register page.
				"""
				response = self.client.get(self.registerUrl)

				self.assertEquals(response.status_code, 200)
				self.assertTemplateUsed(response, 'register.html')

		def testLoginPagePOST(self):
				"""
				This function tests login page.
				"""
				response = self.client.get(self.loginUrl)

				self.assertEquals(response.status_code, 200)
				self.assertTemplateUsed(response, 'login.html')

		# def testLogoutPagePOST(self):
		# 		response = self.client.get(self.logoutUrl)

		# 		self.assertEquals(response.status_code, 200)
		# 		self.assertTemplateUsed(response, 'logout.html')


