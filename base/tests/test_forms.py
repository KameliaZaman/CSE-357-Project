import imp
from django.test import TestCase
from base.forms import *
from django.core.files.uploadedfile import SimpleUploadedFile

class TestForms(TestCase):
    """
	Form testing inherited from TestCase class
	"""

    def testCreateUserFormValidData(self):
        """
        createUserForm form testing method with valid data

        Parameters:
            self: Passes a class related to TestCase
        
        Returns:
            none
        """
        form=createUserForm(data={
            'username':'Tom',
            'email':'tom@mail.com',
            'password1':'tom2022tom',
            'password2':'tom2022tom'
        })

        self.assertTrue(form.is_valid())

    def testCreateUserFormNoData(self):
        """
        createUserForm form testing method with no data

        Parameters:
            self: Passes a class related to TestCase

        Returns:
            none
        """
        form=createUserForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),3)

    def testUploadCodeFormValidData(self):
        """
        uploadCodeForm form testing method with valid data

        Parameters:
            self: Passes a class related to TestCase
        
        Returns:
            none
        """
        upload_file = open('base/tests/codeFile/Factorial.py', 'rb')
        post_dict = {'codeUploadedBy':'Tom','codeName':'Python1'}
        file_dict = {'codeFile': SimpleUploadedFile(upload_file.name, upload_file.read())}
        form = uploadCodeForm(post_dict, file_dict)
        

        self.assertFalse(form.is_valid())

    def testUploadCodeFormNoData(self):
        """
        uploadCodeForm form testing method with no data

        Parameters:
            self: Passes a class related to TestCase
        
        Returns:
            none
        """
        form=uploadCodeForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),3)
