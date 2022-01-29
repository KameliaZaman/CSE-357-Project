
from django.http import response
from django.test import TestCase, Client
from django.urls import reverse
import chatting
from chatting.models import roomModel, messageModel

class TestViews(TestCase):
    '''
    This class test the functions of views.py file

    '''
    def setUp(self):
        '''
        set up client, home_url, room_url,room1 object, checkView_url, getMessage_url, send_url for testing purpose

        '''
        self.client = Client()
        self.home_url = reverse('home')
        self.room_url = reverse('room',args=['Softwere Engineering'])
        self.room1 = roomModel.objects.create(
            name= 'Softwere Engineering'
        )
        self.checkView_url = reverse('checkView')
        self.getMessage_url = reverse('getMessages',args=['Softwere Engineering'])
        self.send_url = reverse('send')

    def test_home_GET(self):
        '''
        This function test the home method of views file

        '''
        response= self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'chatting/home.html')

    def test_room_GET(self):
        '''
        Tests the working of room function

        '''
        response= self.client.get(self.room_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'chatting/room.html')

    def test_checkView_GET(self):
        '''
        tests checkView function

        '''
        response= self.client.get(self.checkView_url)
        self.assertEquals(response.status_code, 302)


    
    def test_getMessage_GET(self):
        '''
        tests working of getMessage function of views file

        '''
        response= self.client.get(self.getMessage_url)
        self.assertEquals(response.status_code, 200)

   

    def test_sendMessage_GET(self):
        '''
        test the function of sendMessage
        
        '''
        response= self.client.get(self.send_url)
        self.assertEquals(response.status_code, 200)
    

    

