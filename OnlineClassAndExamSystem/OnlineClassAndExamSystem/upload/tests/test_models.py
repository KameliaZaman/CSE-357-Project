from unicodedata import name
from django.test import TestCase
from upload.models import questionAndSolution

class TestModels(TestCase):
    def setUp(self):
        self.demo1 = questionAndSolution.objects.create(
            subject ="Web Development",
            semester ="Third year second",
            question = "",
            solution = "dspAnswer_2HJSy4N.pdf")
        
    def test_subject_name_is_set(self):
            self.assertEquals(self.demo1.subject, "Web Development")