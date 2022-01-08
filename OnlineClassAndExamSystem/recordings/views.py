from django.shortcuts import render
from .forms import videoForm
from .models import Video
from django.db.models import Q

def index(request):
    """
    Collect information for an individual :model:`recording.Video`.

    **Context**

    ``Video``
        An instance of :model:`recording.Video`.

    **Template:**

    :template:`recordings/index.html`
    """

    form=videoForm()
    if request.method == "POST":
        form=videoForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            form = videoForm() 
    
    return render(request,'recordings/index.html',{"form":form})

def showVideo(request):
    """
    Display an individual :model:`recording.Video`.

    **Context**

    ``Video``
        An instance of :model:`recording.Video`.

    **Template:**

    :template:`recording/showVideo.html`
    """
    if 'q' in request.GET:
        q=request.GET['q']
        # allVideo=Video.objects.filter(courseName__icontains=q)
        multiple_q =Q(Q(caption__icontains=q)|Q(courseName__icontains=q))
        allVideo = Video.objects.filter(multiple_q)
    
    
    else:
        allVideo=Video.objects.all()
    form=videoForm()
    return render(request,'recordings/showVideo.html',{"form":form,"all":allVideo})



