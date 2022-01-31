from django.test import SimpleTestCase
from django.urls import reverse,resolve
from base.views import *

class TestUrls(SimpleTestCase):
    """
	Url testing inherited from SimpleTestCase class
	"""

    def testRegisterUrlResolves(self):
        """
        Register url testing method

        Parameters:
            self: Passes a class related to SimpleTestCase
        
        Returns:
            none
        """
        url=reverse('register')
        self.assertEquals(resolve(url).func, registerPage)

    def testLoginUrlResolves(self):
        """
        Login url testing method

        Parameters:
            self: Passes a class related to SimpleTestCase
        
        Returns:
            none
        """
        url=reverse('login')
        self.assertEquals(resolve(url).func, loginPage)

    def testLogoutUrlResolves(self):
        """
        Logout url testing method

        Parameters:
            self: Passes a class related to SimpleTestCase
        
        Returns:
            none
        """
        url=reverse('logout')
        self.assertEquals(resolve(url).func, logoutUser)

    def testHomeUrlResolves(self):
        """
        Dashboard url testing method

        Parameters:
            self: Passes a class related to SimpleTestCase
        
        Returns:
            none
        """
        url=reverse('home')
        self.assertEquals(resolve(url).func, home)

    def testUserPageUrlResolves(self):
        """
        User homepage url testing method

        Parameters:
            self: Passes a class related to SimpleTestCase
        
        Returns:
            none
        """
        url=reverse('user-page')
        self.assertEquals(resolve(url).func, userPage)

    def testUserUrlResolves(self):
        """
        User profile url testing method

        Parameters:
            self: Passes a class related to SimpleTestCase
        
        Returns:
            none
        """
        url=reverse('user', args=['some-pk'])
        self.assertEquals(resolve(url).func, profileView)

    def testSubmissionViewUrlResolves(self):
        """
        Submission view url testing method

        Parameters:
            self: Passes a class related to SimpleTestCase
        
        Returns:
            none
        """
        url=reverse('submissionView')
        self.assertEquals(resolve(url).func, submissionViewPage)

    def testUploadCodeUrlResolves(self):
        """
        Code Upload url testing method

        Parameters:
            self: Passes a class related to SimpleTestCase
        
        Returns:
            none
        """
        url=reverse('uploadCode')
        self.assertEquals(resolve(url).func, uploadCode)

    def testRunCodeUrlResolves(self):
        """
        Code run url testing method

        Parameters:
            self: Passes a class related to SimpleTestCase
        
        Returns:
            none
        """
        url=reverse('runCode')
        self.assertEquals(resolve(url).func, runCode)