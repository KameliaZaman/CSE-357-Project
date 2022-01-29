from django.test import SimpleTestCase
from django.urls import reverse,resolve
from recordings.views import index,showVideo

class TestUrls(SimpleTestCase):
    '''
    This class is for testing the urls of recording app
    '''
    def test_index_url_is_resolved(self):
        '''
        This function tests index page url
        '''
        url = reverse('index')
        self.assertEquals(resolve(url).func,index)

    def test_showVideo_url_is_resolved(self):
        '''
        This function tests showVideo page url
        '''
        url = reverse('showVideo')
        self.assertEquals(resolve(url).func,showVideo)

    

    

    

    

