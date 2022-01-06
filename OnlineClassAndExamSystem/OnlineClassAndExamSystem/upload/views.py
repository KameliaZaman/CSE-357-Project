from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from .forms import questionAndSolutionForm
from .models import questionAndSolution
# Create your views here.
class home(TemplateView):
    template_name ='upload/home.html'

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)

def showQuestionAndSolutionList(request):
    q = request.GET.get('q') if request.GET.get('q')!=None  else ''
    quesAndSolutions = questionAndSolution.objects.filter(
        Q(subject__icontains= q)|
        Q(semester__icontains= q)
        )
    return render(request,'quesAndSolveList.html',{'quesAndSolutions':quesAndSolutions})

def uploadQuestionAndSolution(request):
     if request.method == 'POST':
        form = questionAndSolutionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show')
     else:
        form = questionAndSolutionForm()
     return render(request, 'upQuesAndSolveList.html', {
        'form': form})
