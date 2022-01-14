from django.db import models

#username -tisha
#password -tisha123


# Create your models here.
class Video(models.Model):
    """This model is used by a teacher to assign the assignments.

    Attributes:
    ----------
    videoId: Indicates the character fields of video id and creates.
    caption: Indicates the character fields of topic name and creates.
    courseName: Indicates the character fields of course name and creates.
    teacherId: Indicates the integer fields of teacher id and creates.
    video =  Indicates the file fields of video recordings and creates.

    Method:
    ------
    __str__: Returns the caption of the video recording.
    
    
    """

    videoId = models.AutoField(primary_key=True)
    caption=models.CharField(max_length=200)
    courseName = models.CharField(max_length=200, default="")
    teacherId =models.IntegerField(default=0)
    video=models.FileField(upload_to="video/%y")

    def __str__(self):
        return self.caption
        
