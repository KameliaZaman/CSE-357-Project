
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from upload.views import home, showQuestionAndSolutionList,uploadQuestionAndSolution

class TestUrls(SimpleTestCase):
    def test_home_url_is_resolved(self):
        url = reverse('home')
        
        self.assertEquals(resolve(url).func,home )
    
    def test_show_url_is_resolved(self):
        url = reverse('show')
        
        self.assertEquals(resolve(url).func,showQuestionAndSolutionList )
    
    def test_uploadQuesAndSolve_url_is_resolved(self):
        url = reverse('uploadQuesAndSolve')
    
        self.assertEquals(resolve(url).func,uploadQuestionAndSolution)