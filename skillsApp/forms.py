# responsible for defining forms that are used to collect and validate user input.


from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm #django user creation form 
from django.contrib.auth.models import User #django user model
from .models import Colleague, Ticket
from django.utils import timezone



class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    colleagueID = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username','colleagueID', 'first_name', 'last_name', 'email', 'password1', 'password2' )  # Include 'colleagueID' in the fields list

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')

        if commit:
            user.save()
            Colleague.objects.create(
                user=user, 
                first_name=self.cleaned_data.get('first_name'),
                last_name=self.cleaned_data.get('last_name'),
                email=self.cleaned_data.get('email'),
                date_joined=timezone.now(),
                colleagueID=self.cleaned_data.get('colleagueID')  # Set the 'colleagueID' field
            )

        return user
    

class ColleagueForm(forms.ModelForm):
    class Meta:
        model = Colleague
        fields = '__all__'  # This will include all fields in the form
        exclude = ['user', 'date_joined', 'colleagueID', 'status']


#Create Ticket form

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'category', 'summary', 'priority', 'assignee_team', 'status', 'colleague', 'escalated', 'recreate']  # Add 'colleague' to the fields list

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        colleague = kwargs.pop('colleague', None)
        super(TicketForm, self).__init__(*args, **kwargs)
        if user is not None:
            if not user.is_staff:
                del self.fields['status']
                del self.fields['priority']
                del self.fields['assignee_team']
                del self.fields['escalated']
                del self.fields['colleague']  # Exclude the 'colleague' field for standard users
            else:
                if colleague is not None:
                    self.fields['colleague'].initial = colleague


class TicketUpdateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'category', 'summary', 'priority', 'assignee_team', 'status']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(TicketUpdateForm, self).__init__(*args, **kwargs)
        if user is not None and not user.is_staff:
            del self.fields['status']
            del self.fields['priority']
            del self.fields['assignee_team']