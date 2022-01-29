from django.test import TestCase
from django.urls import reverse

class TestViews(TestCase):
    def test_should_show_assignment_page(self):
        response = self.client.get(reverse('showAssignments'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"assignments/showAssignments.html")

    def test_should_pending_assignment_page(self):
        response = self.client.get(reverse('pendingAssignments'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"assignments/pendingAssignments.html")

    def test_should_show_view_submission_page(self):
        response = self.client.get(reverse('viewSubmission'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"assignments/viewSubmission.html")

