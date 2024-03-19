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



#register page, allows users to create an account
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
@login_required
def logoutUser(request):
    logout(request) # use Django method
    return redirect('login')


#CRUD CREATE FUNCTION
@login_required  # Decorator to ensure only logged-in users can access this view
def createTicket(request, colleague_id=None):
    # If a colleague_id is provided, get the Colleague object with that ID
    if colleague_id is not None:
        colleague = get_object_or_404(Colleague, colleagueID=colleague_id)
    else:
        # If the logged-in user is a superuser, set colleague to None
        if request.user.is_superuser:
            colleague = None
        else:
            # Otherwise, set colleague to the Colleague object associated with the logged-in user
            colleague = request.user.colleague

    # If the request method is POST, this means the form is being submitted
    if request.method == 'POST':
        # Create a TicketForm instance with the submitted data
        form = TicketForm(request.POST, user=request.user, colleague=colleague)
        # If the form is valid, save the form but don't commit to the database yet
        if form.is_valid():
            ticket = form.save(commit=False)
            # If colleague is not None, set the ticket's colleague to the selected colleague
            if colleague is not None:
                ticket.colleague = colleague
            # Save the ticket to the database
            ticket.save()
            # Redirect the user to the home page
            return redirect('home')
    else:
        # If the request method is not POST, this means the form is being displayed
        # So create a new TicketForm instance without any data
        form = TicketForm(user=request.user, colleague=colleague)
    # Create the context dictionary
    context = {'form': form}
    # Render the create_ticket.html template with the context
    return render(request, 'skillsApp/create_ticket.html', context)



#CRUD UPDATE FUNCTION, GET ticket and update it
@login_required
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
@login_required
@allowed_users(["admin"])
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
@login_required
@allowed_users(['standard'])
def accountSettings(request):
    return render(request, 'skillsApp/account_settings.html')


@login_required
def colleagues(request, pk):
    colleague = Colleague.objects.get(id=pk)
    form = ColleagueForm(instance=colleague)  # Initialize the form with the 'colleague' instance

    ticket = colleague.ticket_set.all()
    context = {'colleague':colleague, 'ticket':ticket, 'form': form}  # Include the form in the context
    return render(request, 'skillsApp/colleagues.html',context)