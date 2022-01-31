from django.test import TestCase
from base.models import *
from django.contrib.auth.models import User

class TestModels(TestCase):
    """
	Model testing inherited from TestCase class
	"""

    def testUserAccountStr(self):
        """
        userAccount model testing method

        Parameters:
            self: Passes a class related to TestCase
        
        Returns:
            none
        """
        userName=User.objects.create(username="Tom")
        fullName=userAccount.objects.create(fullName="Tom")
        userPhone=userAccount.objects.create(userPhone="12345")
        userEmail=userAccount.objects.create(userEmail="tom@mail.com")

        self.assertEquals(str(userName),"Tom")


    def testSolutionCodeStr(self):
        """
        solutionCode model testing method

        Parameters:
            self: Passes a class related to TestCase
        
        Returns:
            none
        """
        codeUploadedBy=User.objects.create(username="Tom")
        codeName=solutionCode.objects.create(codeName="Python1")
        codeFile=solutionCode.objects.create(codeFile="codeFile/Factorial.py")

        self.assertEquals(str(codeName),"Python1")
        