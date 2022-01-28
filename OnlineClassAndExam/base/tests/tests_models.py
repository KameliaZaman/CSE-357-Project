# from django.test import TestCase
# from django.contrib.auth.models import User
# from main.models import questionModel, responseOnQuestion


# class testModels(TestCase):
#     def setUp(self):
#         self.question1 = questionModel.objects.create(
#             author=User,
#             title='My site'
#         )
#     def testQuestionModel(self):
#         author = questionModel.objects.get(author=User)
#         title = questionModel.objects.get(title='My site')

#         self.assertEquals(author, User)
#         self.assertEquals(title, 'This is my site')