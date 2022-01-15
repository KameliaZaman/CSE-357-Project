from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
from .models import *
from .forms import  createUserForm
from .decorators import unauthenticatedUser, allowedUsers, adminOnly

@unauthenticatedUser
def registerPage(request):
	"""
	Display register page :model:'userAccount'.

	**Context**
	''form''
		An instance of :model:'createUserForm.User'.

	**Template:**
	:template:'accounts/register.html'
	"""
	form = createUserForm()
	if request.method == 'POST':
		form = createUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			#group = Group.objects.get(name='user')
			#user.groups.add(group)
			userAccount.objects.create(
				userName=user,
				fullName=user.username,
				)

			messages.success(request, 'Account was created for ' + username)

			return redirect('login')
		

	context = {'form':form}
	return render(request, 'accounts/register.html', context)

@unauthenticatedUser
def loginPage(request):
	"""
	Display login page :model:' '.

	**Context**
	''none''

	**Template:**
	:template:'accounts/login.html'
	"""
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'accounts/login.html', context)

def logoutUser(request):
	"""
	Display login page after logging out :model:' '.

	**Context**
	''none''

	**Template:**
	:template:'accounts/login.html'
	"""
	logout(request)
	return redirect('login')

@login_required(login_url='login')
@adminOnly
def home(request):
	"""
	Display home page for teachers :model:'userAccount'.

	**Context**
	''users''
		An instance of :model:'userForm.User'.

	**Template:**
	:template:accounts/dashboard.html'
	"""
	users = userAccount.objects.all()
	context={'users':users}
	return render(request, 'accounts/dashboard.html',context)

@login_required(login_url='login')
@allowedUsers(allowedRoles=['student'])
def userPage(request):
	"""
	Display home page for students :model:' '.

	**Context**
	''none''

	**Template:**
	:template:accounts/user.html'
	"""
	return render(request, 'accounts/user.html')


@login_required(login_url='login')
@allowedUsers(allowedRoles=['admin'])
def profileView(request, pk_test):
	user = userAccount.objects.get(id=pk_test)

	context = {'user':user}
	return render(request, 'accounts/profile.html',context)
