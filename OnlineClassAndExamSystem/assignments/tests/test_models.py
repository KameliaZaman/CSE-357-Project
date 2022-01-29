from django.test import TestCase
from assignments.models import AssignmentsUpload,AssignmentsSubmit

class TestModels(TestCase):
    '''
    This class test models.py file
    '''
    def test_uploadAssignment(self):
        '''
        Sets assingmentupload object for testing purpose

        '''
        assignmentupload=AssignmentsUpload(courseName="Software Engineering",topicName="Documentation",submissionDate="2022-01-27",submissionTime="16:33:00",files="files/22/Lec-10Digital_interfacing_Last_Part.pdf")
        assignmentupload.save()
        self.assertEqual(str(assignmentupload),'Documentation')

    def test_assignmentSubmit(self):
        '''
        Sets assignmentsubmit object for testing purpose

        '''
        assignmentssubmit=AssignmentsSubmit(studentName="Fatima",studentId="222",questionFile="files/22/4th_Ed_Ch10-pointer_WXXlvHW.pdf",answerFile="files/22/ArtGallleryNew.ppt",submitTime="2022-01-13 17:18:31")
        assignmentssubmit.save()
        self.assertEqual(str(assignmentssubmit),'Fatima - 222')