from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class userAccount(models.Model):
	"""
	This model stores user accounts entry, related to: model:'auth.User'.

	**Attributes**
    --------------
    userName: Indicates the character field of user name from User.
    fullName: Indicates the character field of user's full name.
    userPhone: Indicates the character field of user's phone number.
    userEmail: Indicates the character field of user email.
    dateCreated =  Indicates the date-time field of user account creation time.

    **Method**
    ----------
    __str__: Returns the title of user account.
	"""
	userName = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	fullName = models.CharField(max_length=200, null=True)
	userPhone = models.CharField(max_length=200, null=True)
	userEmail = models.CharField(max_length=200, null=True)
	dateCreated = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return str(self.userName)

class solutionCode(models.Model):
	"""
	This model stores solution codes.

	**Attributes**
    --------------
    codeUploadedBy: Indicates the foreign key from User model.
    codeName: Indicates the character field of code name.
    codeFile: Indicates the file field of code's solution file.

    **Method**
    ----------
    __str__: Returns the title of solution code.
	"""
	codeUploadedBy=models.ForeignKey(User, null=True,on_delete = models.CASCADE)
	codeName=models.CharField(max_length=100, null=True)
	codeFile=models.FileField(upload_to='codeFile/', null=True)

	def __str__(self):
		return self.codeName