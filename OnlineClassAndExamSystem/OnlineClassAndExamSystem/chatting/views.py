from django.core.checks import messages
from django.http import request
from django.shortcuts import redirect, render
from chatting.models import roomModel,messageModel
from django.http import HttpResponse,JsonResponse

# Create your views here.
def home(request):
    return render(request,'chatting/home.html')
    
def room(request,room):
    userName = request.GET.get('username')
    roomDetails = roomModel.objects.get(name = room)
    return render(request, 'chatting/room.html',{
        'username' : userName,
        'room': room,
        'roomDetails': roomDetails
    })

def checkView(request):
    room = request.POST['room_name']
    userName = request.POST['username']

    if roomModel.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+userName)
    else:
        newRoom = roomModel.objects.create(name=room)
        newRoom.save()
        return redirect('/'+room+'/?username='+userName)

def sendMessage(request):
    message = request.POST['message']
    userName = request.POST['username']
    roomId = request.POST['room_id']
    newMessage = messageModel.objects.create(value= message, user= userName, room = roomId)
    newMessage.save()
    return HttpResponse('Message is sent successfully')

def getMessages(request, room):
    roomDetails = roomModel.objects.get(name= room)
    messages = messageModel.objects.filter(room= roomDetails.id)
    return JsonResponse({"messages": list(messages.values())})
