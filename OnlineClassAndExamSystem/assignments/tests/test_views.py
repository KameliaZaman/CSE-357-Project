from django.test import TestCase
from django.urls import reverse

class TestViews(TestCase):
   
    '''
    This class test the functions of views.py file
    '''
    
    def test_showAssignment_page(self):
        '''
        This function test the showAssignment method of views file
        '''
       
        response = self.client.get(reverse('showAssignments'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"assignments/showAssignments.html")

    def test_pendingAssignment_page(self):
        '''
        This function test the pendingAssignment method of views file
        
        '''
        response = self.client.get(reverse('pendingAssignments'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"assignments/pendingAssignments.html")


    def test_viewSubmission_page(self):
        '''
        This function test the viewAssignment method of views file
        
        '''
        response = self.client.get(reverse('viewSubmission'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"assignments/viewSubmission.html")

