from django.db import models

#username -tisha
#password -tisha123

# Create your models here.
class Video(models.Model):
    videoId = models.AutoField(primary_key=True)
    caption=models.CharField(max_length=200)
    courseName = models.CharField(max_length=200, default="")
    teacherId =models.IntegerField(default=0)
    video=models.FileField(upload_to="video/%y")

    def __str__(self):
        return self.caption
        
