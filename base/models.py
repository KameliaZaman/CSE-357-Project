from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class userAccount(models.Model):
	userName = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	fullName = models.CharField(max_length=200, null=True)
	userPhone = models.CharField(max_length=200, null=True)
	userEmail = models.CharField(max_length=200, null=True)
	dateCreated = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return str(self.userName)

class blog(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User,on_delete = models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    def get_absolute_url(self):
        #return reverse('blog-detail', args=(str(self.id)))
        return reverse('blog')