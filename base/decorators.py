from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticatedUser(viewFunc):
	"""
	Method for unregistered and ungrouped persons

	Parameter:
		viewFunc ([String]): [passes a page to check whether person can access]

	Returns: 
		none

	Method: 
		wrapperFunc: Checks whether a person can view certain pages.

		Parameter: 
			request ([String]): [creates a request to view any page], 
			*args ([String]): [condition to enter], 
			**kwargs ([String]): [current values]

		Returns: 
			[String]: [decision of whether person can access]
	"""
	def wrapperFunc(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('home')
		else:
			return viewFunc(request, *args, **kwargs)

	return wrapperFunc

def allowedUsers(allowedRoles=[]):
	"""
	Method for registered users

	Parameter: 
		allowedRoles[] ([String]): [passes value if a person is associated to any group]

	Returns: 
		none

	Method: 
		decorator: Method for restriction in groups

		Parameter: 
			viewFunc ([String]): [passes a page to check whether a group can access]

		Returns: 
			[String]: [restricted or not]

		Method: 
			wrapperFunc: Checks whether a group is restricted to view any page.

			Parameter: 
				request ([String]): [creates a request to view any page], 
				*args ([String]): [condition to enter], 
				**kwargs ([String]): [current values]

			Returns: 
				[String]: [decision of whether a group can access]
	"""
	def decorator(viewFunc):
		def wrapperFunc(request, *args, **kwargs):
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
	Method for only admins to view

	Parameter: 
		viewFunc ([String]): [passes a page for only admin to access]

	Returns:
		none

	Method: 
		wrapperFunction: Decides which page a group sees after logging in.

			Parameter: 
				request ([String]): [creates a request to view any page], 
				*args ([String]): [condition to enter], 
				**kwargs ([String]): [current values]

			Returns: 
				[String]: [decision of whether a group can access]
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