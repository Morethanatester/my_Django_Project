from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout # for login functionality
from django.contrib import messages #django flash messages -- https://docs.djangoproject.com/en/3.0/ref/contrib/messages/#using-messages-in-views-and-templates
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import QueryDict
from django.shortcuts import get_object_or_404
from .models import Colleague
from .forms import ColleagueForm
from django import forms

from .decorators import unauthenticated_user, allowed_users, admin_only
#Import all(*) project models/forms
from .models import *
from .forms import * 

@login_required()
def home(request):
    tickets = Ticket.objects.all()
    colleagues = Colleague.objects.all()

    context = {'tickets':tickets, 
               'colleagues':colleagues} 

    if request.user.is_staff:
        # Render the admin dashboard
        return render(request, 'skillsApp/admin_dashboard.html', context)
    else:
        tickets = Ticket.objects.filter(colleague=request.user.colleague)
        context = {'tickets':tickets, 
               'colleagues':colleagues}
        # Render the standard user dashboard
        return render(request, 'skillsApp/standard_dashboard.html', context)



def faults(request):
    return render(request, 'skillsApp/faults.html')


@login_required()
def settings(request):
    if request.method == 'POST':
        form = ColleagueForm(request.POST, instance=request.user.colleague)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your settings have been updated.')
            return redirect('home')
    else:
        form = ColleagueForm(instance=request.user.colleague)
    context = {'form': form}
    return render(request, 'skillsApp/settings.html', context)





    return render(request, 'skillsApp/settings.html')




#register page, allows users to create an account
''' TODO, not implemented'
@unauthenticated_user
'''
@unauthenticated_user
def registerPage(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, f"{field.label}: {error}")
    else:
        form = RegisterForm()
    context = {'form': form}
    return render(request, 'skillsApp/register.html', context)


#login page, allows users to login
@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'skillsApp/login.html', context)

#logout page, allows users to logout
def logoutUser(request):
    logout(request) # use Django method
    return redirect('login')

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



#@login_required
#CRUD CREATE FUNCTION

def createTicket(request, colleague_id=None):
    if colleague_id is not None:
        colleague = get_object_or_404(Colleague, colleagueID=colleague_id)
    else:
        colleague = request.user.colleague

    if request.method == 'POST':
        form = TicketForm(request.POST, user=request.user, colleague=colleague)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.colleague = request.user.colleague
            ticket.save()
            return redirect('home')
    else:
        form = TicketForm(user=request.user, colleague=colleague)
    context = {'form': form}
    return render(request, 'skillsApp/create_ticket.html', context)



#CRUD UPDATE FUNCTION, GET ticket and update it
def updateTicket(request, pk):
    ticket = Ticket.objects.get(id=pk)
    if request.user.is_staff or request.user == ticket.colleague.user:
        form = TicketUpdateForm(instance=ticket, user=request.user)
        if request.method == 'POST':
            form = TicketUpdateForm(request.POST, instance=ticket, user=request.user)
            if form.is_valid():
                form.save()
                return redirect('home')
        context = {'form': form}
        return render(request, 'skillsApp/update_ticket.html', context)
    else:
        return redirect('home')
    

#CRUD DELETE FUNCTION, GET ticket and delete it
def deleteTicket(request, pk):
    if request.user.is_staff:
        ticket = Ticket.objects.get(id=pk)
        if request.method == 'POST':
            ticket.delete()
            return redirect('home')
        context = {'item': ticket}
        return render(request, 'skillsApp/delete_ticket.html', context)
    else:
        return redirect('home')




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


'''
not yet implemented
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
'''
def colleagues(request, pk):
    colleague = Colleague.objects.get(id=pk)
    form = ColleagueForm(instance=colleague)  # Initialize the form with the 'colleague' instance

    ticket = colleague.ticket_set.all()
    context = {'colleague':colleague, 'ticket':ticket, 'form': form}  # Include the form in the context
    return render(request, 'skillsApp/colleagues.html',context)