from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticatedUser(viewFunc):
	"""
	Method for unregistered and ungrouped persons
	"""
	def wrapperFunc(request, *args, **kwargs):
		"""
		Checks whether a person can view certain pages.
		"""
		if request.user.is_authenticated:
			return redirect('home')
		else:
			return viewFunc(request, *args, **kwargs)

	return wrapperFunc

def allowedUsers(allowedRoles=[]):
	"""
	Method for registered users
	"""
	def decorator(viewFunc):
		def wrapperFunc(request, *args, **kwargs):
			"""
			Checks whether a user is restricted to view any page
			"""
			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name

			if group in allowedRoles:
				return viewFunc(request, *args, **kwargs)
			else:
				return HttpResponse('You are not authorized to view this page')
		return wrapperFunc
	return decorator

def adminOnly(viewFunc):
	"""
	Method for admins
	"""
	def wrapperFunction(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == 'student':
			return redirect('user-page')

		if group == 'admin':
			return viewFunc(request, *args, **kwargs)

	return wrapperFunction