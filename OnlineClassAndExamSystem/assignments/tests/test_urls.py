from django.test import SimpleTestCase
from django.urls import reverse,resolve
from assignments.views import uploadAssignments,showAssignments,pendingAssignments,viewSubmission,submissionPage

class TestUrls(SimpleTestCase):
    def test_uploadassignment_url_is_resolved(self):
        url = reverse('uploadAssignments')
        self.assertEquals(resolve(url).func,uploadAssignments)

    def test_showassignment_url_is_resolved(self):
        url = reverse('showAssignments')
        self.assertEquals(resolve(url).func,showAssignments)

    def test_pendingassignment_url_is_resolved(self):
        url = reverse('pendingAssignments')
        self.assertEquals(resolve(url).func,pendingAssignments)

    def test_viewsubmission_url_is_resolved(self):
        url = reverse('viewSubmission')
        self.assertEquals(resolve(url).func,viewSubmission)


    

    

    

