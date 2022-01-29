from django.test import TestCase
from recordings.models import Video

class TestModels(TestCase):
    def test_should_upload_assignment(self):
        videoup=Video(videoId="1",caption="Coding Standard",courseName="Software Engineering",teacherId="3",video="video/22/sample-10s_vKsi2wi.mp4")
        videoup.save()
        self.assertEqual(str(videoup),'Coding Standard')

