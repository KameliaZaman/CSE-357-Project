from django.test import TestCase
from django.urls import reverse

class TestViews(TestCase):
    def test_should_show_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"recordings/index.html")

    def test_should_show_video_page(self):
            response = self.client.get(reverse('showVideo'))
            self.assertEqual(response.status_code,200)
            self.assertTemplateUsed(response,"recordings/showVideo.html")



    
