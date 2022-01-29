from django.test import SimpleTestCase
from upload.forms import questionAndSolutionForm

class TestForms(SimpleTestCase):

    def test_ques_solution_form_no_data(self):
        form = questionAndSolutionForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),3)