from django.db import models

from django.contrib.auth.models import AbstractUser,User

# Create your models here.

class userAccount(models.Model):
    """This model creates user account.
    Attributes:
    ----------
    userName: Indicates the character fields of user and creates.
    userEmail: Indicates the character fields of email and creates.
    userPassword: Indicates the character fields of password and creates.

    Method:
    ------
    __str__: Returns the name of the user.
    """
    userName = models.CharField(max_length=200, null=True)
    userEmail = models.EmailField(unique=True, null=True)
    userPassword = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.userName

class discussionTopic(models.Model):
    """This model creates discussion topic.
    Attributes:
    ----------
    topicName: Indicates the character fields of topic and creates.

    Method:
    ------
    __str__: Returns the name of the topic.
    """
    topicName = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.topicName


class discussionRoom(models.Model):
    """This model creates discussion room.
    Attributes:
    ----------
    host: Get generated as foreign key inherits from User.
    topicName: Get generated as foreign key inherits from discussionTopic.
    roomName: Indicates the character fields of room and creates.
    roomPrivacy = Indicates the character fields of room privacy and creates.
    romDescription = Indicates the text fields of room description and creates.
    roomParticipants: Indicate many to many relation inherits from User.
    roomUpdated: Indicate the time room is updated.
    roomCreated: Indicate the time room is created.

    Method:
    ------
    __str__: Returns the name of the user.

    Class:
    -----
    Ordering is basically is used to change the order of model fields.
    """
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
    """This model creates message on each topic in any discussion channel.
    Attributes:
    ----------
    username: Get generated as foreign key inherited from UserAccount.
    roomName: Get generated as foreign key inherited from discussionRoom.
    messageBody: Indicate the message body of any discussion inside any certain room.
    messageUpdated: Indicate the time of updating messages.
    messageCreated: Indicate the time of creating messages.
    """
    userName = models.ForeignKey(userAccount, on_delete=models.CASCADE)
    roomName = models.ForeignKey(discussionRoom, on_delete=models.CASCADE)
    messageBody = models.TextField()
    messageUpdated = models.DateTimeField(auto_now=True)
    messageCreated = models.DateTimeField(auto_now_add=True)
