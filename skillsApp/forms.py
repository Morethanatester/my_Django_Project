# responsible for defining forms that are used to collect and validate user input.


from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm #django user creation form 
from django.contrib.auth.models import User #django user model
from .models import Colleague
from django.utils import timezone



class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

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
                date_joined=timezone.now()
            )

        return user
    

class ColleagueForm(forms.ModelForm):
    class Meta:
        model = Colleague
        fields = '__all__'  # This will include all fields in the form
        exclude = ['user', 'date_joined', 'colleagueID', 'status']

