from django.db import models
from django.contrib.auth.models import AbstractUser,User

# Create your models here.

class userAccount(models.Model):
    userName = models.CharField(max_length=200, null=True)
    userEmail = models.EmailField(unique=True, null=True)
    userPassword = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.userName

class discussionTopic(models.Model):
    topicName = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.topicName


class discussionRoom(models.Model):
    roomPrivacy=(
        ('private','private'),
        ('public','public'),
    )
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topicName = models.ForeignKey(discussionTopic, on_delete=models.SET_NULL, null=True)
    roomName = models.CharField(max_length=200,null=True, blank=True)
    roomPrivacy= models.CharField(max_length=200,null=True,choices=roomPrivacy)
    roomDescription = models.TextField(null=True, blank=True)
    roomParticipants = models.ManyToManyField(
        User, related_name='roomParticipants', blank=True)
    roomUpdated = models.DateTimeField(auto_now=True)
    roomCreated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-roomUpdated', '-roomCreated']

    def __str__(self):
        return str(self.roomName)


class messageOnTopic(models.Model):
    userName = models.ForeignKey(userAccount, on_delete=models.CASCADE)
    roomName = models.ForeignKey(discussionRoom, on_delete=models.CASCADE)
    messageBody = models.TextField()
    messageUpdated = models.DateTimeField(auto_now=True)
    messageCreated = models.DateTimeField(auto_now_add=True)