from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout # for login functionality
from django.contrib import messages #django flash messages -- https://docs.djangoproject.com/en/3.0/ref/contrib/messages/#using-messages-in-views-and-templates



#Import all(*) project models/forms
from .models import *
from .forms import * 

def home(request):
    return render(request, 'skillsApp/dashboard.html')

def faults(request):
    return render(request, 'skillsApp/faults.html')

def Settings(request):
    return render(request, 'skillsApp/settings.html')

def loginPage(request):

    if request.method == 'POST':
        

        #get values from field from login.html page
        username = request.POST.get('username') 
        password = request.POST.get('password')

        #authenticate user exists in database
        user = authenticate(request, username=username, password=password) 
        
        #if user exists redirect to homepage
        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            messages.info(request, 'username OR password is incorrect')

    context = {}
    return render(request, 'skillsApp/login.html', context)

def logoutUser(request):
    logout(request) # use Django method
    return redirect('login')


#accountsettings page, allows users to update profile info

''' TODO, not implemented
#@login_required(login_url='login')
#@allowed_users(allowed_roles=['user'])
'''
def accountSettings(request):
    return render(request, 'skillsApp/account_settings.html')

'''
	user = request.user.colleague
	form = ColleagueForm(instance=user)

	if request.method == 'POST':
		form = ColleagueForm(request.POST, request.FILES,instance=user)
		if form.is_valid():
			form.save()

	context = {'form':form}
    return render(request, 'skillsApp/settings.html', context)
'''
#CRUD views


#HANDLES CREATE CRUD FUNCTION, PASSED INTO DASHBOARD HTML CREATE FAULT BUTTON

