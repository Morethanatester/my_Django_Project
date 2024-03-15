from django.http import HttpResponse
from django.shortcuts import redirect

# A decorator in Python is a callable that wraps a function to extend its behavior 
# without permanently modifying it. It's a powerful tool for modifying the behavior 
# of functions or classes.

#****************restrict an authenticated user, viewing login/regiter page *********************

#if authententicated redirect to 'home' else call view_function where decorator is used
def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('home') 
		else:
			return view_func(request, *args, **kwargs)
	return wrapper_func

#********************** allow pages for Allowed users on******************

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            if 'admin' in allowed_roles and request.user.is_staff:
                print("working:", allowed_roles)
                return view_func(request, *args, **kwargs)
            elif 'standard' in allowed_roles and not request.user.is_staff:
                print("working:", allowed_roles)
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')
        return wrapper_func
    return decorator

#*******************redirects if user to correct URL/function****************************

def admin_only(view_func):
	def wrapper_function(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == 'user':
			return redirect('user-page')

		if group == 'admin':
			return view_func(request, *args, **kwargs)

	return wrapper_function