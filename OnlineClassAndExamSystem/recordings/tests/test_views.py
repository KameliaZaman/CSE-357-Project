from django.test import TestCase
from django.urls import reverse

class TestViews(TestCase):
    '''
    This class test the functions of views.py file
    '''
    def test_index_page(self):
        '''
        This function test the index method of views file

        '''
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"recordings/index.html")

    def test_showVideo(self):
        '''
        This function test the showVideo method of views file

        '''
        response = self.client.get(reverse('showVideo'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"recordings/showVideo.html")



    
