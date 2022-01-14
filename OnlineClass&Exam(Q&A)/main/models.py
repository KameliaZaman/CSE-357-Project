from django.db import models
from django.contrib.auth.models import User

"""Online Class And Examination (Q&A feature)
    @Author- Umma Salma
"""

# Create your models here.
class questionModel(models.Model):
    """
    ** Class: **
    ------------
       This model class creates a question model.
			 
       ** Attributes: **
	-----------------
	author: Indicates the author name of the question and gets generated as foreign key inherited from User. 
	title: Indicates the title of the whole question.  
	body: Describes the body of the question.    
	questionCreatedAt: Indicates the time of the creation of certain question. 
	questionUpdatedAt: Indicates the time of the update of certain question.    

	** Methods: **
	--------------
        __str__: Returns the title of the question.  
	get_responses: Returns the response of the question.
    """


    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=False)
    body = models.TextField(null=False)
    questionCreatedAt = models.DateTimeField(auto_now_add=True)
    questionUpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_responses(self):
        return self.responses.filter(parent=None)

class responseOnQuestion(models.Model):
"""
** Class **
-----------
   This model class creates a response-on-question class.

   ** Attributes: **
   -----------------
   user: Indicates the authenticated user name of the respondent and gets generated as foreign key inherited from User.
   question: Inherits the question from the questionModel class and gets generated as foreign key inherited from questionModel model. 
   parent: Indicates the parent response of the question and gets generated as foreign key.
   body: Describes the whole body of the response.
   responseCreatedAt: Indicates the time of the response of certain question.
   responseUpdatedAt: Indicates the time of the update of certain question.

   ** Methods: **
   --------------
   __str__: Returns the body of the response. 
   get_responses: Returns the response of the question.

"""
	user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
	question = models.ForeignKey(questionModel, null=False, on_delete=models.CASCADE, related_name='responses')
	parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
	body = models.TextField(null=False)
	responseCreatedAt = models.DateTimeField(auto_now_add=True)
	responseUpdatedAt = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.body

	def get_responses(self):
		return responseOnQuestion.objects.filter(parent=self)
