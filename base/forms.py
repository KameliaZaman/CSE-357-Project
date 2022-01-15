from statistics import mode
from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class createUserForm(UserCreationForm):
	"""
	Register page form inherited from UserCreationForm
	
	Class: 
		Meta: Used to change the values of User model fields.
	
	Class attributes: 
		model: Name of the model,
		fields: Fields of the model
	"""
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class uploadCodeForm(forms.ModelForm):
	"""
	Code upload form inherited from ModelForm of forms
	
	Class:
		Meta: Used to change the values of solutionCode model fields.
	
	Class attributes:
		model: Name of the model,
		fields: Fields of the model
	"""
	class Meta:
		model=solutionCode
		fields=('codeUploadedBy','codeName','codeFile')