from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import questionModel, responseOnQuestion
from .forms import registerUserForm, loginForm, newQuestionForm, newResponseForm, newReplyForm

# Create your views here.

def registerPage(request):
	""" This function creates register page.

	Parameter:
		request ([String]): [create a request of registration]

	Returns:
		[String]: [renders register page]
	"""
	
	"""
	Import registeruserForm() method from forms.py.
	"""
	form = registerUserForm()

	if request.method == 'POST':
		try:
		 	form = registerUserForm(request.POST)
			if form.is_valid():
				user = form.save()
				login(request, user)
				return redirect('index')
		except Exception as e:
			print(e)
			raise
	context = {
		'form': form
	}

	"""
	** Templates: **
	----------------
	:template: `register.html`
	"""
	return render(request, 'register.html', context)

def loginPage(request):
	"""This function creates login page.

	parameter:
		request ([String]): [creates a request of login page]

	Returns:
		[String]: [renders login page]
	"""

	"""
	Import loginForm() method from forms.py.
	"""
	form = loginForm()

	if request.method == 'POST':
		try:
			form = loginForm(data=request.POST)
			if form.is_valid():
					user = form.get_user()
					login(request, user)
					return redirect('index')
		except Exception as e:
			print(e)
			raise


	"""
	** Attributes: **
	-----------------
	context: Indicates the newly created form.
	"""
	context = {'form': form}

	"""
	** Templates: **
	----------------
	:template: `login.html`
	"""
	return render(request, 'login.html', context)


"""
@login_required: This decorator indicates that, user must be logged in to log out.
"""
@login_required(login_url='register')
def logoutPage(request):
	"""This function creates logout page.

	Parameter:
		request ([String]): [creates a request of logout page]

	Returns:
		[String]: [redirects login page]
	"""
	logout(request)

	"""
	** Templates: **
	----------------
	:template: `login.html`
	"""
	return redirect('login')


"""
@login_required: This decorator indicates that, user must be logged in to create question.
"""
@login_required(login_url='register')
def newQuestionPage(request):
	"""This function creates a new question page.

	parameter:
		request ([String]): [creates a request of new question creation page]

	Returns:
		[String]: [renders new question page]
	"""

	"""
	Import newQuestionForm() method from forms.py.
	"""	
	form = newQuestionForm()

	if request.method == 'POST':
		try:
			form = newQuestionForm(request.POST)
			if form.is_valid():
				question = form.save(commit=False)
				question.author = request.user
				question.save()
		except Exception as e:
			print(e)
			raise


	"""
	** Attributes: **
	-----------------
	context: Indicates the newly created question form.
	"""
	context = {'form': form}

	"""
	** Templates: **
	----------------
	:template: `new-question.html`
	"""
	return render(request, 'new-question.html', context)


def homePage(request):
	""" This function creates homepage.

	Parameter:
		request ([String]): [creates a request of home page]

	Returns:
		[String]: [renders home page]
	"""

	"""
	** Attributes: **
	-----------------
	questions: Indicates ordering of creation of new questions that appears first inherited from questionModel.
	context: Indicates the newly created question.
	"""
	questions = questionModel.objects.all().order_by('-questionCreatedAt')
	context = {
      'questions': questions
    }

	"""
	** Templates: **
	----------------
	:template: `homePage.html`
	"""
	return render(request, 'homepage.html', context)


def questionPage(request, id):
	""" This function creates new question page.

	parameter:
		request ([String]): [creates a request of question page]
		id ([int]): [creates question id]

	Returns:
		[String]: [renders question page]
	"""

	"""
	Import newResponseForm() method from forms.py.
	Import newReplyForm() method from forms.py.
	"""
	response_form = newResponseForm()
	reply_form = newReplyForm()

	if request.method == 'POST':
		try:
			response_form = newResponseForm(request.POST)
			if response_form.is_valid():
				response = response_form.save(commit=False)
				response.user = request.user
				response.question = questionModel(id=id)
				response.save()
				return redirect('/question/'+str(id)+'#'+str(response.id))
		except Exception as e:
			print(e)
			raise


	"""
	** Attributes: **
	-----------------
	question: Indicates the newly created question id inherited from questionModel.
	context: Indicates thenewly created question, response form and reply form.
	"""
	question = questionModel.objects.get(id=id)
	context = {
        'question': question,
        'response_form': response_form,
        'reply_form': reply_form,
    }

	"""
	** Templates: **
	----------------
	:template: `question.html`
	"""
	return render(request, 'question.html', context)



"""
@login_required: This decorator indicates that, user must be logged in to reply question.
"""
@login_required(login_url='register')
def replyPage(request):
	"""This function creates reply page.

	Parameter:
		request ([String]): [creates a request of reply page]

	Returns:
		[String]: [redirects to index page]
	"""
	if request.method == 'POST':
		try:
			form = newReplyForm(request.POST)
			if form.is_valid():
				question_id = request.POST.get('question')
				parent_id = request.POST.get('parent')
				reply = form.save(commit=False)
				reply.user = request.user
				reply.question = questionModel(id=question_id)
				reply.parent = responseOnQuestion(id=parent_id)
				reply.save()
				return redirect('/question/'+str(question_id)+'#'+str(reply.id))
		except Exception as e:
			print(e)
			raise
	"""
	** Templates: **
	----------------
	:template: `index`
	"""
	return redirect('index')
