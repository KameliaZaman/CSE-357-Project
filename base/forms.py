from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class userForm(ModelForm):
	"""
	Login page form
	"""
	class Meta:
		model = userAccount
		fields = '__all__'
		exclude = ['user']


class createUserForm(UserCreationForm):
	"""
	Register page form
	"""
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']