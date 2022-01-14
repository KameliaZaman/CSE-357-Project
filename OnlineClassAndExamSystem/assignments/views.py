from django.shortcuts import render

from .forms import dateForm,submissionForm
from .models import AssignmentsSubmit, AssignmentsUpload
from django.db.models import Q

def uploadAssignments(request):
    """
    This is the assignment uploading page for the teachers.
	Args: 
		([String]): [request]	
	Returns:
		[String]: [render Assignment Uploading page]
	
	** Templates: **
	:template: `assignments/uploadAssignments.html`

    """
    form=dateForm() 
    if request.method == "POST":
        form=dateForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            form = dateForm() 
    
    return render(request,'assignments/uploadAssignments.html',{"form":form})

def showAssignments(request):
    """
    This is the page to view the uploaded page for the teachers.
	Args: 
		([String]): [request]	
	Returns:
		[String]: [render Assignment View page for teachers]
	
		
	** Templates: **
	:template: `assignments/showAssignments.html`
    """
    if 'q' in request.GET:
        q=request.GET['q']
        multiple_q =Q(Q(courseName__icontains=q)|Q(topicName__icontains=q))
        allFiles = AssignmentsUpload.objects.filter(multiple_q)
    else:
        allFiles=AssignmentsUpload.objects.all()
    return render(request,'assignments/showAssignments.html',{"all":allFiles})

def pendingAssignments(request):
    """
    This is the view page of pending Assignments for the students.
	Args: 
		([String]): [request]	
	Returns:
		[String]: [render pending Assignments view page]
	

	** Templates: **
	:template: `assignments/pendingAssignments.html`

    """

    allFiles=AssignmentsUpload.objects.all()
    return render(request,'assignments/pendingAssignments.html',{"all":allFiles})

def submissionPage(request):
    """
    This is the assignment submission page for the students.
	Args: 
		([String]): [request]	
	Returns:
		[String]: [render Assignment submission page]
	

	** Templates: **
	:template: `assignments/submissionPage.html`

    """

    form=submissionForm() 
    if request.method == "POST":
        form=submissionForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            form = submissionForm() 
    
    return render(request,'assignments/submissionPage.html',{"form":form})

def viewSubmission(request):
    """
    This is the view page of all the submission done by the students for the teachers.
	Args: 
		([String]): [request]	
	Returns:
		[String]: [render view submission  page]
	

	** Templates: **
	:template: `assignments/viewSubmission.html`

    """

    allFiles=AssignmentsSubmit.objects.all()
    return render(request,'assignments/viewSubmission.html',{"all":allFiles})








