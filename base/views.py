
import datetime
import json
import os

import requests
from .models import CustomUser



from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.views.generic import ListView, DetailView, CreateView, UpdateView  
# Create your views here.
from .models import *
from .forms import  createUserForm
from .decorators import unauthenticatedUser, allowedUsers, adminOnly



@unauthenticatedUser
def registerPage(request):

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
	logout(request)
	return redirect('login')

@login_required(login_url='login')
@adminOnly
def home(request):
	users = userAccount.objects.all()
	context={'users':users}
	return render(request, 'accounts/dashboard.html',context)

@login_required(login_url='login')
@allowedUsers(allowedRoles=['student'])
def userPage(request):
	
	return render(request, 'accounts/user.html')

class blogView(ListView):
    model = blog
    template_name='accounts/blog.html'
    

class blogDetailView(DetailView):
    model = blog
    template_name='accounts/blogDetails.html'

class addBlogView(CreateView):
    model = blog
    template_name='accounts/addBlog.html'
    fields = '__all__'

class updateBlogView(UpdateView):
	model = blog
	template_name = 'accounts/updateBlog.html'
	fields = ['title','body']




def showFirebaseJS(request):
    data='importScripts("https://www.gstatic.com/firebasejs/7.14.6/firebase-app.js");' \
         'importScripts("https://www.gstatic.com/firebasejs/7.14.6/firebase-messaging.js"); ' \
         'var firebaseConfig = {' \
         '        apiKey: "YOUR_API_KEY",' \
         '        authDomain: "FIREBASE_AUTH_URL",' \
         '        databaseURL: "FIREBASE_DATABASE_URL",' \
         '        projectId: "FIREBASE_PROJECT_ID",' \
         '        storageBucket: "FIREBASE_STORAGE_BUCKET_URL",' \
         '        messagingSenderId: "FIREBASE_SENDER_ID",' \
         '        appId: "FIREBASE_APP_ID",' \
         '        measurementId: "FIREBASE_MEASUREMENT_ID"' \
         ' };' \
         'firebase.initializeApp(firebaseConfig);' \
         'const messaging=firebase.messaging();' \
         'messaging.setBackgroundMessageHandler(function (payload) {' \
         '    console.log(payload);' \
         '    const notification=JSON.parse(payload);' \
         '    const notificationOption={' \
         '        body:notification.body,' \
         '        icon:notification.icon' \
         '    };' \
         '    return self.registration.showNotification(payload.notification.title,notificationOption);' \
         '});'

    return HttpResponse(data,content_type="text/javascript")