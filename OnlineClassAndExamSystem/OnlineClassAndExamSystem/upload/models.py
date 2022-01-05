from django.db import models

# Create your models here.
class questionAndSolution(models.Model):
    subject = models.CharField(max_length=100)
    semester= models.CharField(max_length=100)
    question = models.FileField(upload_to='questionAndSolution/question/',null=True,blank=True)
    solution = models.FileField(upload_to='questionAndSolution/solution/')
    def __str__(self):
        return self.subject