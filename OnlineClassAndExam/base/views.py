from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import discussionTopic, discussionRoom, messageOnTopic
from .forms import roomForm

from django.db.models import Q
# Create your views here.

def homePage(request):
    return render(request, 'base/homePage.html')


def topicsPage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    discussTopic = discussionTopic.objects.filter(name__icontains=q)
    return render(request, 'base/topics.html', {'topics': discussTopic})

def room(request, pk):
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

    context = {'room': room, 'room_messages': roomMessages,
               'participants': participants}
    return render(request, 'base/room.html', context)

def createRoomSingleton(request):
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

    context = {'form': form, 'topics': topics}
    return render(request, 'base/roomForm.html', context)

def updateRoomSingleton(request, pk):
    room = discussionRoom.objects.get(id=pk)
    form = roomForm(instance=room)
    topics = discussionTopic.objects.all()
    if request.user != room.host:
        return HttpResponse('Your are not allowed here!!')

    if request.method == 'POST':
        topicName = request.POST.get('topic')
        topicCreated = discussionTopic.objects.get_or_create(name=topicName)
        room.name = request.POST.get('name')
        room.topic = topicCreated
        room.description = request.POST.get('description')
        room.save()
        return redirect('base/homePage')

    context = {'form': form, 'topics': topics, 'room': room}
    return render(request, 'base/roomForm.html', context)

def deleteRoomSingleton(request, pk):
    room = discussionRoom.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse('Your are not allowed here!!')

    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})

def deleteMessageSingleton(request, pk):
    message = messageOnTopic.objects.get(id=pk)

    if request.user != message.user:
        return HttpResponse('Your are not allowed here!!')

    if request.method == 'POST':
        message.delete()
        return redirect('homePage')
    return render(request, 'base/delete.html', {'obj': message})

def activityPageSingleton(request):
    roomMessages = messageOnTopic.objects.all()
    return render(request, 'base/activity.html', {'room_messages': roomMessages})