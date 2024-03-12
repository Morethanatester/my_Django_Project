# responsible for defining forms that are used to collect and validate user input.


from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm #django user creation form 
from django.contrib.auth.models import User #django user model
from .models import Colleague


#HANDLES CREATE CRUD FUNCTION
class ColleagueForm(ModelForm):
	class Meta:
		model = Colleague
		#fields = ['name','email','tel','status'] 
		fields = ['name','email',] 
		exclude = ['user']

