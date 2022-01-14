from django.shortcuts import render
from .forms import videoForm
from .models import Video
from django.db.models import Q

def index(request):
    """
    This is the index page to upload class recording by the teacher.
	Args: 
		([String]): [request]	
	Returns:
		[String]: [render class recording Uploading page]
	
	** Templates: **
	:template: `recordings/index.html`

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
    This is the page for viewing all uploaded video for the teachers and students.
	Args: 
		([String]): [request]	
	Returns:
		[String]: [render Video viewing page]
	
	** Templates: **
	:template: `recordings/showVideo.html`

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



