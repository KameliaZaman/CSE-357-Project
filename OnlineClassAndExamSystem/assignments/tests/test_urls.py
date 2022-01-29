from django.test import SimpleTestCase
from django.urls import reverse,resolve
from assignments.views import uploadAssignments,showAssignments,pendingAssignments,viewSubmission,submissionPage

class TestUrls(SimpleTestCase):

    '''   
    This class is for testing the urls of assignment app
  
    '''
    def test_uploadAssignment_url_is_resolved(self):
        '''
        This function tests uploadAssignments page url

        '''
        url = reverse('uploadAssignments')
        self.assertEquals(resolve(url).func,uploadAssignments)

    def test_showAssignment_url_is_resolved(self):
        '''
        This function tests showAssignments page url
        '''
        url = reverse('showAssignments')
        self.assertEquals(resolve(url).func,showAssignments)

    def test_pendingAssignment_url_is_resolved(self):
        '''
        This function tests pendingAssignment page url

        '''
        url = reverse('pendingAssignments')
        self.assertEquals(resolve(url).func,pendingAssignments)

    def test_viewSubmission_url_is_resolved(self):
        '''
        This function tests viewSubmission page url
        
        '''
        url = reverse('viewSubmission')
        self.assertEquals(resolve(url).func,viewSubmission)


    

    

    

