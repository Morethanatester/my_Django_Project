from django.db import models
from django import forms
from django.contrib.auth.models import User # django user model


# Create your models here.


class Colleague(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    date_joined = models.DateTimeField(null=True)
    tel = models.CharField(max_length=15, null=True)  # Telephone number
    colleagueID = models.CharField(max_length=100, null=True)  # Colleague ID
    jobfamily = models.CharField(max_length=100, null=True)  # Job family
    status = models.CharField(max_length=100, null=True)  # Status

    def save(self, *args, **kwargs):
        if self.user:
            user_current = User.objects.get(id=self.user.id)
            if self.first_name != user_current.first_name:
                self.user.first_name = self.first_name
            if self.last_name != user_current.last_name:
                self.user.last_name = self.last_name
            if self.email != user_current.email:
                self.user.email = self.email
            #if self.date_joined != user_current.date_joined:
            #    self.user.date_joined = self.date_joined
            self.user.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
'''
class Keyword(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name
'''

        
class Ticket(models.Model):
    # ...

    colleague = models.ForeignKey(Colleague, null=True, on_delete=models.CASCADE)

    # ...
