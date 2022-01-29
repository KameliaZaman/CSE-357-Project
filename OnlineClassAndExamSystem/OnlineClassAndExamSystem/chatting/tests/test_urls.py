from django.test import SimpleTestCase
from django.urls import reverse, resolve
from chatting.views import home, room, checkView,sendMessage, getMessages

class TestUrls(SimpleTestCase):

    '''
    This class is for testing the urls of chatting app

    '''

    def test_home_url_is_resolved(self):
        '''
        this fuction tests home page url

        '''
        url = reverse('home')
        self.assertEquals(resolve(url).func,home)
    
    def test_room_urls_is_resolved(self):
        '''
        This function test room page url

        '''
        url = reverse('room', args=['some-str'])
        self.assertEquals(resolve(url).func, room)

    def test_checkView_url_is_resolved(self):
        '''
        Checks if checkView function url is correct

        '''
        url = reverse('checkView')
        self.assertEquals(resolve(url).func,checkView)
    
    def test_sendMessage_url_is_resolved(self):
        '''
        Checks sendView url is correct or not

        '''
        url = reverse('send')
        self.assertEquals(resolve(url).func,sendMessage)

    def test_getMessage_url_is_resolved(self):
        '''
        checks getMessage view url
        
        '''
        url = reverse('getMessages',args=['some-str'])
        self.assertEquals(resolve(url).func,getMessages)
