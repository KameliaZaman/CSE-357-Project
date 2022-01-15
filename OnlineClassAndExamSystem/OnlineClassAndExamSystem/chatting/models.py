from django.db import models
from datetime import datetime


class roomModel(models.Model):
    """
    A class used to represent a roomModel table in the database.
    Stores the name of the rooms.
    ....

    Attributes
    ----------

    name : CharFiled
        Name of chatting room

    Methods
    -------

    __str__(self)
        Prints the name of the room

    """
    name = models.CharField(max_length= 1000)
    def __str__(self):
        return self.name

class messageModel(models.Model):
    """
    A class used to represent a messageModel table in database.
    Using this table we can store and retrive message related all the information.
    ....

    Attributes
    ----------

    value : CharFiled
        Message send via a user
    date : DateTimeField
        Indicate the time when the message is sent
    user : CharFiled
        Name of the user who has send the message
    room : CharFiled
        Name of the chatting room.

    """
    value= models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)
