from django.db import models

#username -tisha
#password -tisha123


# Create your models here.
class Video(models.Model):
    """
    Stores a single video entry,it's all about the video's cation,the course name realted to
    the video, and the teacher id who's uploading and the model is related to :model:...
    """

    videoId = models.AutoField(primary_key=True)
    caption=models.CharField(max_length=200)
    courseName = models.CharField(max_length=200, default="")
    teacherId =models.IntegerField(default=0)
    video=models.FileField(upload_to="video/%y")

    def __str__(self):
        """
         Parameters
        ----------
        name : self
            Indicate the class itself
         Returns
        ----------
            Show the video caption in the database"""
        return self.caption
        
