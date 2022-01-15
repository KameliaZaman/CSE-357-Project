from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import registerPage, loginPage, logoutPage, homePage, newQuestionPage, questionPage, replyPage

class testUrls(SimpleTestCase):
		"""
		This class is a test class of Urls inherited from SimpleTestCase.
		"""

		def testRegisterUrlResolves(self):
				"""
				This function tests register url.
				"""
				url = reverse('register')
				self.assertEquals(resolve(url).func, registerPage)

		def testLoginUrlResolves(self):
				"""
				This function tests login url.
				"""
				url = reverse('login')
				self.assertEquals(resolve(url).func, loginPage)

		def testLogoutUrlResolves(self):
				"""
				This function tests logout url.
				"""
				url = reverse('logout')
				self.assertEquals(resolve(url).func, logoutPage)

		def testHomeUrlResolves(self):
				"""
				This function tests home url.
				"""
				url = reverse('index')
				self.assertEquals(resolve(url).func, homePage)

		def testNewQuestionUrlResolves(self):
				"""
				This function tests new question url.
				"""
				url = reverse('new-question')
				self.assertEquals(resolve(url).func, newQuestionPage)

    # def testQuestionUrlResolves(self):
    #     url = reverse('question', args=['some-id'])
    #     self.assertEquals(resolve(url).func, questionPage)

		def testReplyUrlResolves(self):
				"""
				This function tests reply url.
				"""
				url = reverse('reply')
				self.assertEquals(resolve(url).func, replyPage)




