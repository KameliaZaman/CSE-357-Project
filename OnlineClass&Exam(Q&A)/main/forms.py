from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import questionModel, responseOnQuestion
from django import forms

class registerUserForm(UserCreationForm):
	""" This class creates user registration form inherited from User creation form.

			** Class: **
			------------
			Meta: Model Meta is basically used to change the behavior of model fields.

			** Class attributes: **
			-----------------------
			model: Name of the model.
			fields: fields of the model.
			widgets: widget is Django’s representation of an HTML input element.
	"""
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		widgets = {
				'email': forms.EmailInput(attrs={
        'required': True,
        'placeholder': 'lisa@example.com',
        'autofocus': True
        }),
        'username': forms.TextInput(attrs={
        'placeholder': 'lisamora',
        	})
        }


		"""
		** Method: **
		-------------
		__init__: This method is called when an object is created from a class and it allows the class to initialize the attributes of the class.
		"""
		def __init__(self, *args, **kwargs):
			super(registerUserForm, self).__init__(*args, **kwargs)
			self.fields['password1'].widget.attrs = {'placeholder': 'password'}
			self.fields['password2'].widget.attrs = {'placeholder': 'confirm password'}


class loginForm(AuthenticationForm):
	"""
	This class creates user login form inherited from Authentication form.
	"""
	class Meta:
		fields = '__all__'

class newQuestionForm(forms.ModelForm):
	"""
	This class creates new question form inherited from Model Form.
	"""
	class Meta:
		model = questionModel
		fields = ['title', 'body']
		widgets = {
        'title': forms.TextInput(attrs={
        'autofocus': True,
				'placeholder': 'How to create a Q&A website with Django?'
          })
        }

class newResponseForm(forms.ModelForm):
	"""
	This class creates new response form inherited from Model Form.
	"""
	class Meta:
		model = responseOnQuestion
		fields = ['body']

class newReplyForm(forms.ModelForm):
	"""
	This class creates new reply form inherited from Model Form.
	"""
	class Meta:
		model = responseOnQuestion
		fields = ['body']
		widgets = {
				'body': forms.Textarea(attrs={
				'rows': 2,
				'placeholder': 'What are your thoughts?'
        	})
        }
