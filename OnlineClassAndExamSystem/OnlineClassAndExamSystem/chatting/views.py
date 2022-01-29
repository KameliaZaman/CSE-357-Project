from django.core.checks import messages
from django.http import request
from django.shortcuts import redirect, render
from chatting.models import roomModel,messageModel
from django.http import HttpResponse,JsonResponse


def home(request):
    """
    Display a basic home page

    **Context**

    "none"

    **Template:**

    Returns response to home.html template
    """
    return render(request,'chatting/home.html')
    
def room(request,room):
    """
    Accepts room name and username from the url of room page and filter out information
    using those name.

    **Context**

    "userName"
        [string] : Name of a particular user of messageModel class
    "roomDetails"
        [list] : Filter out all the the room details that matches the name
    "room"
        [string] : Name of a particular room recived from room page url

    **Template:**

    Returns response to room.html template
    """
    userName = request.GET.get('username')
    roomDetails = roomModel.objects.get(name = room)
    return render(request, 'chatting/room.html',{
        'username' : userName,
        'room': room,
        'roomDetails': roomDetails
    })

def checkView(request):
    """
    Receives request from the home page and send this info to the room page

    **Context**

    "room"
        [string]: Specific room name send via a POST method
    "userName"
        [string]: specific username send via a POST method

    **Template:**

    Returns response to room.html template with room and username as a parameter
    """
    room = request.POST.get('room_name',False)
    #room = request.POST['room_name']
    #userName = request.POST['username']
    userName = request.POST.get('username',False)

    if roomModel.objects.filter(name=room).exists():
        return redirect('/'+str(room)+'/?username='+str(userName))
    else:
        newRoom = roomModel.objects.create(name=room)
        newRoom.save()
        return redirect('/'+str(room)+'/?username='+str(userName))

def sendMessage(request):
    """
    Takes data that is send via ajax method and save it to the database

    **Context**

    "message"
        [string]: Messages send from the room page.
    "userName"
        [string]: Name of that particular user who has sent the message.
    "roomId":
        [string]: Id of that particular room from which the data is sent.
    "newMessage"
        [messageModel] : An instance of messageModel class

    Returns:

    returns a HttpResponse if the data is saved successfully
    """ 
    message = request.POST.get('message', False)
    #message = request.POST['message']
    #userName = request.POST['username']
    #roomId = request.POST['room_id']
    userName = request.POST.get('username', False)
    roomId = request.POST.get('room_id', False)


    newMessage = messageModel.objects.create(value= message, user= userName, room = roomId)
    newMessage.save()
    return HttpResponse('Message is sent successfully')

def getMessages(request, room):
    """
    Filter out all the messages of a particular room and send them to the room page

    **Context**

    "roomDetails"
        [list] : Filter out all the the room details that matches the name
    "messages"
        [list] : List of all messages of a particular room

    Returns:

    Returns JsonResponse with a list o messages to room page
    """
    roomDetails = roomModel.objects.get(name= room)
    messages = messageModel.objects.filter(room= roomDetails.id)
    return JsonResponse({"messages": list(messages.values())})
