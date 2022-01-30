from django.test import TestCase
from base.models import blog


class TestModels(TestCase):

    def setUp(self):
        self.blog = blog.objects.create(
            title = 'blog 1 ',
            author = 'Kazi Muhammad',
            body = 'This is a test case '

        )

    def testBlogisAssignedSlugOnCreation(self):
        self.assertEquals(self.blog.slug, 'blog-1')