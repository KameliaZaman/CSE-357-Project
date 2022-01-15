from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import registerPage, loginPage, logoutPage, homePage, newQuestionPage, questionPage, replyPage

class testUrls(SimpleTestCase):

    def testRegisterUrlResolves(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, registerPage)

    def testLoginUrlResolves(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, loginPage)

    def testLogoutUrlResolves(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logoutPage)

    def testHomeUrlResolves(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, homePage)

    def testNewQuestionUrlResolves(self):
        url = reverse('new-question')
        self.assertEquals(resolve(url).func, newQuestionPage)

    # def testQuestionUrlResolves(self):
    #     url = reverse('question', args=['some-id'])
    #     self.assertEquals(resolve(url).func, questionPage)

    def testReplyUrlResolves(self):
        url = reverse('reply')
        self.assertEquals(resolve(url).func, replyPage)




