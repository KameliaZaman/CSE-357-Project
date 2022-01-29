from django.test import SimpleTestCase
from django.urls import reverse,resolve
from recordings.views import index,showVideo

class TestUrls(SimpleTestCase):
    def test_uploadassignment_url_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func,index)

    def test_showassignment_url_is_resolved(self):
        url = reverse('showVideo')
        self.assertEquals(resolve(url).func,showVideo)

    

    

    

    

