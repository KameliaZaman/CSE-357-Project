from django.db import models
from django.utils import timezone
from datetime import date

# admin - tisha12345
# pass -tisha12345

class AssignmentsUpload(models.Model):
    """This model is used by a teacher to assign the assignments.

    Attributes:
    ----------
    courseName: Indicates the character fields of coursename and creates.
    topicName: Indicates the character fields of topic name and creates.
    submissionDate: Indicates the date fields of date and creates.
    submissionTime =  Indicates the time fields of time and creates.
    files =  Indicates the file fields of file and creates.

    Method:
    ------
    is_past_due() : Returns a true if the submission date is ahead of today otherwise false. 
    __str__: Returns the name of the user.
    
    
    """
    courseName = models.CharField(max_length=50)
    topicName = models.CharField(max_length=200)
    submissionDate = models.DateField()
    submissionTime = models.TimeField()
    files = models.FileField(upload_to="files/%y")

    @property
    def is_past_due(self):
        return date.today() < self.submissionDate


    def __str__(self):
        return self.topicName



class AssignmentsSubmit(models.Model):
    """This model is used to store all the assignment's files submitted by
    the students and a teacher will have view access of it.

    Attributes:
    ----------
    studentName: Indicates the character fields of student name and creates.
    studentName: Indicates the character fields of student id and creates.
    questionFile: Indicates the file fields of question and creates.
    submissionTime =  Indicates the character fields of time and creates.
    files =  Indicates the character fields of file and creates.

    Method:
    ------
    __str__: Returns the name and id of the student.
    
    
    """

    studentName = models.CharField(max_length=50)
    studentId = models.CharField(max_length=100)
    questionFile = models.FileField(upload_to="files/%y")
    answerFile = models.FileField(upload_to="files/%y")
    submitTime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.studentName + " - "+self.studentId
