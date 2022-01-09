from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from .forms import questionAndSolutionForm
from .models import questionAndSolution
# Create your views here.
def home(request):
    """
    Display a basic home page

    **Context**

    **Template:**

    :template:'home.html'
    """
    return render(request,'home.html')

def showQuestionAndSolutionList(request):
    """
    Gets a html request object. Filter out all the information according to the request 
    and pass the result to a template to show those in a form of
    table. Use a model :model:'upload.questionAndSolution'.

    **Context**

    "quesAndSolutions"
        An instance of :model:'upload.questionAndSolution'.

    **Template:**

    :template:'quesAndSolveList.html'
    """
    q = request.GET.get('q') if request.GET.get('q')!=None  else ''
    quesAndSolutions = questionAndSolution.objects.filter(
        Q(subject__icontains= q)|
        Q(semester__icontains= q)
        )
    return render(request,'quesAndSolveList.html',{'quesAndSolutions':quesAndSolutions})

def uploadQuestionAndSolution(request):
    """
    Receives valus from a form. Validate the form data and than save to the database if they are valid.
    Use a model :model:'upload.questionAndSolution'.

    **Context**

    "form"
        An instance of :form:'upload.questionAndSolutionForm'.

    **Template:**

    :template:'upQuesAndSolveList.html'
    """
    if request.method == 'POST':
        form = questionAndSolutionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show')
    else:
        form = questionAndSolutionForm()
    return render(request, 'upQuesAndSolveList.html', {
        'form': form})
