from django.db import models
from django.contrib.auth.models import User # django user model

# Create your models here.





class Colleague(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    date_joined = models.DateTimeField(null=True)

    # Rest of the fields for the Colleague model

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

    colleague = models.ForeignKey(Colleague, null=True, on_delete=models.SET_NULL)

    # ...
