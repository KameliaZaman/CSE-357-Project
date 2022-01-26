from django.test import SimpleTestCase
from upload.forms import questionAndSolutionForm

class TestForms(SimpleTestCase):
    def test_quses_solution_form_valid_data(self):
        form = questionAndSolutionForm(data={
            "subject" : "Operating System",
            "semester" : "Third Year First",
            "question" : "",
            "solution" : "dspAnswer_2HJSy4N.pdf"

        })

        self.assertTrue(form.is_valid())

    def test_ques_solution_form_no_data(self):
        form = questionAndSolutionForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),3)