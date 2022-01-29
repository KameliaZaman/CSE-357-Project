from django.test import TestCase
from recordings.models import Video

class TestModels(TestCase):
    '''
    This class test models.py file
    '''
    def test_Video(self):
        '''
        Sets Video object for testing purpose  
        '''
        videoup=Video(videoId="1",caption="Coding Standard",courseName="Software Engineering",teacherId="3",video="video/22/sample-10s_vKsi2wi.mp4")
        videoup.save()
        self.assertEqual(str(videoup),'Coding Standard')

