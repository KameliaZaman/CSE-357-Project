import sys
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
from .forms import  createUserForm, uploadCodeForm
from .decorators import unauthenticatedUser, allowedUsers, adminOnly

from django.db.models import Q

@unauthenticatedUser
def registerPage(request):
	"""
	Display register page :model:'userAccount'.

	Parameter:
		request ([String]): [create a request of register page]

	Returns:
		[String]: [renders register page]

	Context:
		''form''
			An instance of :model:'createUserForm.User'.

	Template:
		:template:'accounts/register.html'
	"""
	form = createUserForm()
	if request.method == 'POST':
		form = createUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			userAccount.objects.create(
				userName=user,
				fullName=user.username,
				userEmail=user.email,
				)

			messages.success(request, 'Account was created for ' + username)

			return redirect('login')
		

	context = {'form':form}
	return render(request, 'accounts/register.html', context)

@unauthenticatedUser
def loginPage(request):
	"""
	Display login page :model:' '.

	Parameter:
		request ([String]): [create a request of login page]

	Returns:
		[String]: [renders login page]

	Context:
		''none''

	Template:
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

	Parameter:
		request ([String]): [create a request of login page]

	Returns:
		[String]: [redirects to login page]

	Context:
		''none''

	Template:
		:template:'accounts/login.html'
	"""
	logout(request)
	return redirect('login')

@login_required(login_url='login')
@adminOnly
def home(request):
	"""
	Display home page for teachers :model:'userAccount'.

	Parameter:
		request ([String]): [create a request of dashboard page]

	Returns:
		[String]: [renders dashboard page]

	Context:
		''users''
			An instance of :model:'userForm.User'.

	Template:
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

	Parameter:
		request ([String]): [create a request of user page]

	Returns:
		[String]: [renders user page]

	Context:
		''none''

	Template:
		:template:accounts/user.html'
	"""
	return render(request, 'accounts/user.html')


@login_required(login_url='login')
@allowedUsers(allowedRoles=['admin'])
def profileView(request, pk_test):
	"""
	Display profile viewing page for teacher :model:'userAccount'.

	Parameter:
		request ([String]): [create a request of profile page],
		pk_test ([String]): [passes primary key value for selected user profile]

	Returns:
		[String]: [renders profile page]

	Context:
		''user''
			An instance of :model:'userForm.User'.

	Template:
		:template:accounts/profile.html'
	"""
	user = userAccount.objects.get(id=pk_test)

	context = {'user':user}
	return render(request, 'accounts/profile.html',context)


@login_required(login_url='login')
@allowedUsers(allowedRoles=['admin'])
def submissionViewPage(request):
	"""
	Display submissions by student for teacher :model:'solutionCode'.

	Parameter:
		request ([String]): [create a request of submission view page]

	Returns:
		[String]: [renders submission view page]

	Context:
		''none''

	Template:
		:template:accounts/submissionView.html'
	"""
	q = request.GET.get('q') if request.GET.get('q')!=None  else ''
	solutionCodes = solutionCode.objects.filter(
		Q(codeName__icontains= q)
        )
	return render(request,'accounts/submissionView.html',{'solutionCodes':solutionCodes})


@login_required(login_url='login')
@allowedUsers(allowedRoles=['student'])
def uploadCode(request):
	"""
	Display upload codes page for student :model:' '.

	Parameter:
		request ([String]): [create a request of upload code page]

	Returns:
		[String]: [renders upload code page]

	Context:
		''none''

	Template:
		:template:accounts/uploadCode.html'
	"""
	if request.method == 'POST':
		form = uploadCodeForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			messages.info(request, 'File uploaded successfully.')
	else:
		form = uploadCodeForm()
	return render(request, 'accounts/uploadCode.html', {
        'form': form})


@login_required(login_url='login')
@allowedUsers(allowedRoles=['admin'])
def runCode(request):
	"""
	Display this page when code runs for teacher :model:' '.

	Parameter:
		request ([String]): [create a request of submission view page]

	Returns:
		[String]: [renders submission view page]

	Context:
		''none''

	Template:
		:template:accounts/submissionView.html'
	"""
	if request.method == "POST":
		codeAreaData = request.POST['codearea']
		try:
			original_stdout = sys.stdout
			sys.stdout = open('file.txt', 'w')
			exec(codeAreaData)
			sys.stdout.close()
			sys.stdout = original_stdout
			output = open('file.txt', 'r').read()
			
		except Exception as e:
			sys.stdout = original_stdout
			output = e
	return render(request , 'accounts/submissionView.html', {"code":codeAreaData , "output":output})
