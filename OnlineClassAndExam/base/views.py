from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import discussionTopic, discussionRoom, messageOnTopic
from .forms import roomForm

from django.db.models import Q

"""Online Class And Examination system
	 @Author: Umma Salma
"""

# Create your views here.

def homePage(request):

	"""This is the home page of our site.
	Args: 
		([String]): [request]	

	Returns:
		[String]: [render home page]
	"""
		
	"""
	** Templates: **
	:template: `base/homePage.html`
	"""
	return render(request, 'base/homePage.html')


def topicsPage(request):
	""" This function shows all the disscussion topics.

	Args:
		request ([String]): [request]

	Attributes:
	----------
	q: Indicate the parameter of GET method.
	discussTopic: Indicate the all discussion topic objects.

	Returns:
		[String]: [renders topics page]
	"""
	q = request.GET.get('q') if request.GET.get('q') != None else ''
	discussTopic = discussionTopic.objects.filter(name__icontains=q)
	"""
	** Templates **
	:template: `base/topics.html`
	"""
	return render(request, 'base/topics.html', {'topics': discussTopic})


	
def room(request, pk):
	""" This function created room of discussion.

	Args:
		request ([String]): [request]
		pk ([int]): [returns id]

	Attributes:
	----------
	room: Creates room.
	roomMessages: Creates and shows all the room messages.
	participants: Shows all the participants of the room.

	Returns:
		[String]: [redirects to home page]
	"""
	room = discussionRoom.objects.get(id=pk)
	roomMessages = room.message_set.all()
	participants = room.participants.all()

	if request.method == 'POST':
		message = messageOnTopic.objects.create(
    user=request.user,
    room=room,
    body=request.POST.get('body')
		     )
		room.participants.add(request.user)
	return redirect('room', pk=room.id)

	"""
	** Templates: **
	:template: `base/room.html`
	"""

	context = {'room': room, 'room_messages': roomMessages,
               'participants': participants}
	return render(request, 'base/room.html', context)


def createRoom(request):
	""" This function creates room of discussion.

	Args:
		request ([String]): [request]

	Attributes:
	----------
	form: Imports roomForm() method.
	topics: Indicate the all discussion topic of the room.

	Returns:
		[String]: [renders room form page]
	"""
	
	"""
	** Context **
	form: An instance of :model:'roomForm.User'.
	"""
	form = roomForm()
	topics = discussionTopic.objects.all()
	if request.method == 'POST':
		topicName = request.POST.get('topicName')
		topicName, roomCreated = discussionTopic.objects.get_or_create(topicName=topicName)

		discussionRoom.objects.create(
			host=request.user,
			topicName=topicName,
			roomName=request.POST.get('roomName'),
			roomDescription=request.POST.get('roomDescription'),
		)
		return redirect('base/homePage')
	"""
	** Templates: **
	:template: `base/roomForm.html`
	"""
	context = {'form': form, 'topics': topics}
	return render(request, 'base/roomForm.html', context)

def updateRoom(request, pk):
	""" This function updates room of discussion.

	Args:
		request ([String]): [request]
		pk ([int]): [returns room id]

	Attributes:
	----------
	room: gets all the discussion room id.
	form: creates a roomForm instance.
	topics: Gets all the discussion topic.

	Returns:
			[String]: [renders home page]
	"""
	room = discussionRoom.objects.get(id=pk)
	form = roomForm(instance=room)
	topics = discussionTopic.objects.all()

	""" If user is not registered, user can not update room."""
	if request.user != room.host:
		return HttpResponse('Your are not allowed here!!')

	if request.method == 'POST':
		"""POST method creates topic inside the room."""
		topicName = request.POST.get('topic')
		topicCreated = discussionTopic.objects.get_or_create(name=topicName)
		room.name = request.POST.get('name')
		room.topic = topicCreated
		room.description = request.POST.get('description')
		room.save()
		return redirect('base/homePage')
		"""
			** Templates: **
		:template: `base/roomForm.html`
		"""
	context = {'form': form, 'topics': topics, 'room': room}
	return render(request, 'base/roomForm.html', context)

def deleteRoom(request, pk):
	"""Authenticated user can delete rooms.

	Args:
		request ([String]): [request]
		pk ([id]): [returns room id]

	Returns:
		[String]: [render delete page]
	"""
	room = discussionRoom.objects.get(id=pk)

	if request.user != room.host:
		return HttpResponse('Your are not allowed here!!')

	if request.method == 'POST':
		room.delete()
		return redirect('home')
		
		"""
		** Templates: **
		:template: `base/delete.html`
		"""
	return render(request, 'base/delete.html', {'obj': room})

def deleteMessage(request, pk):
	""" Authenticated user can delete messages inside the room.

	Args:
		request ([String]): [request]
		pk ([int]): [returns room id]

	Returns:
		[String]: [renders delete page]
	"""
	message = messageOnTopic.objects.get(id=pk)

	if request.user != message.user:
		return HttpResponse('Your are not allowed here!!')

	if request.method == 'POST':
		message.delete()
		return redirect('homePage')
		"""
			** Templates: **
		:template: `base/delete.html`
		"""
	return render(request, 'base/delete.html', {'obj': message})

def activityPage(request):
	""" Shows the recent activity page.

	Args:
		request ([String]): [request]
	Attributes:
	---------
	roomMessages: Gets all the certain room messages.

	Returns:
		[String]: [renders activity page]
	"""
	roomMessages = messageOnTopic.objects.all()
	return render(request, 'base/activity.html', {'room_messages': roomMessages})
