from django.db import models

# Create your models here.
class questionAndSolution(models.Model):
    """
    A class used to represent a questionAndSolution table in database.
    Using this table we can store and retrive questions and solutions related
    information.

    ...

    Attributes
    ----------
    subject : CharFiled
        Indicate the name of the subject related to a question
    semester : CharFiled
        Gives information about which semester's question it is 
    question : FileFiled
        This file object will be be saved to the location specified by the upload to argument during saving
    solution : FileFiled
        Takes solution file and saved to the database

    Methods
    -------
    __str__(self)
        Prints the name of the subject
    """
    subject = models.CharField(max_length=100)
    semester= models.CharField(max_length=100)
    question = models.FileField(upload_to='questionAndSolution/question/',null=True,blank=True)
    solution = models.FileField(upload_to='questionAndSolution/solution/')
    def __str__(self):
        return self.subject