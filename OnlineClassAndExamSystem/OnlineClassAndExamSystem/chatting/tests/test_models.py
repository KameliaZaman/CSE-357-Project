from django.test import TestCase
from chatting.models import roomModel, messageModel

class TestModels(TestCase):
    '''
    Tests the models

    '''
    def setUp(self):
        '''
        Sets self.room1 object for testing purpose

        '''
        self.room1 = roomModel.objects.create(
            name='Softwere Engineering'
        )
        

    def test_room_name(self):
        '''
        test the working of  __str__ function
        '''
        self.assertEquals(self.room1.name,'Softwere Engineering')