from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout # for login functionality
from django.contrib import messages #django flash messages -- https://docs.djangoproject.com/en/3.0/ref/contrib/messages/#using-messages-in-views-and-templates
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Colleague
from django import forms


#Import all(*) project models/forms
from .models import *
from .forms import * 

def home(request):
    return render (request, 'skillsApp/dashboard.html')

'''
    faults = Ticket.objects.all()
    colleagues = Colleague.objects.all()


    #used to print data onto the dashboard cards through status, count is just counting all
    total_resolved = colleagues.count() #TODO, needs to filter total faults resolved not colleagues and changed in status.html to show correct data
    total_faults = faults.count()
    outstanding = faults.filter(status='Triage').count() #TODO, needs to filter just open tickets
    filtered_faults = faults.filter(category='Software').count()


    context = {'faults':faults, 'colleagues':colleagues,
               'total_resolved': total_resolved,
               'total_faults': total_faults, 
               'outstanding': outstanding,
               'filtered_faults':filtered_faults } 

    return render(request, 'skillsApp/dashboard.html', context)
'''




def faults(request):
    return render(request, 'skillsApp/faults.html')

def Settings(request):
    return render(request, 'skillsApp/settings.html')


def loginPage(request):
    return render(request, 'skillsApp/login.html')


'''
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
'''




''' TODO, not implemented'
@unauthenticated_user
'''
'''
def registerPage(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #get username from form attributes
            username = form.cleaned_data.get('username') 
            messages.success(request, "Account created for " + username ) #temporarily displays messages 
            return redirect("login") #returns to login after registering
    else:
        form = UserCreationForm()
    context = {'form':form} #pass form into context
    return render(request, 'skillsApp/register.html', context)

class ColleagueForm(forms.ModelForm):
    class Meta:
        model = Colleague
        fields = ['first_name', 'last_name', 'email', 'date_joined']
'''

def registerPage(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    else:
        form = RegisterForm()
    context = {'form': form}
    return render(request, 'skillsApp/register.html', context)

'''
    #middleware refactoring, have to do this if/else for every class needed to restrict logged in users viewing a page
    #commented out because decorator unauthenticated_user now doing this
    #if request.user.is_authenticated: #django user creation form
    #    return redirect ('home') #removes register page for logged in user
#else:
    form = CreateUserForm()
    #if method = POST send that data to CreateUserForm, then is the form is valid save it
    if request.method == 'POST':
        form =  CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username') #get username only from form attributes

            group = Group.objects.get(name='user')#automatically assocaiates new users with user group...NOT admin
            user.groups.add(group)
            Colleague.objects.create(
                user=user,
            )



            messages.success(request, "Account created for " + username ) #temporarily displays messages 

            return redirect("login") #returns to login after registering
    context = {'form':form}
    return render(request,'ticket_app/register.html', context)
'''


''' TODO, not implemented
@login_required(login_url='login')
@allowed_users(allowed_roles=['user'])
'''
def userPage(request):
    return render (request, 'skillsApp/user.html')
    '''
    ticket = request.user.colleague.ticket_set.all()
    total_faults = ticket.count()
    filtered_faults = ticket.filter(status='Triage').count()
    context = {'ticket':ticket, 'total_faults':total_faults, 'filtered_faults':filtered_faults}
    
    return render(request, 'ticket_app/user.html', context)
    '''



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



''' TODO, not implemented
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
'''
'''
def deleteFault(request, pk):
	fault = Ticket.objects.get(id=pk) 
	if request.method == "POST":
		fault.delete() #CRUD DELETE FUNCTION, GET variable fault and delete it
		return redirect('/')

	context = {'item':fault}
	return render(request, 'ticket_app/delete.html', context)
'''
#HANDLES CREATE CRUD FUNCTION, PASSED INTO DASHBOARD HTML CREATE FAULT BUTTON

