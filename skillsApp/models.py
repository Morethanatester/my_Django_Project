from django.db import models
from django import forms
from django.contrib.auth.models import User # django user model
from django.utils.crypto import get_random_string


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


    #DEFINE DROP DOWNS
    CATEGORY = (
        ('Software', 'Software'),
        ('Laptop', 'Laptop'),
        ('Desktop', 'Desktop'),
        ('Headphones', 'Headphones'),
        ('Monitor', 'Monitor'),
        ('Keyboard', 'Keyboard'),
        ('Mouse', 'Mouse'),
        ('Other', 'Other'),
    )

    PRIORITY = (
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low')
    )

    RESOLVERS = (
        ('Development Team', 'Development Team'),
        ('Management', 'Management'),
        ('Product Owner', 'Product Owner'),
        ('Suppliers', 'Suppliers'),
    )

    STATUS = (
        ('Triage', 'Triage'),
        ('Open', 'Open'),
        ('Rejected', 'Rejected'),
        ('Fix in Progress', 'Fix in Progress'),
        ('Resolution', 'Resolution'),
        ('Resolved','Resolved'),
        ('Closed', 'Closed'),
    )

    TEAM = (
    ('Development Team', 'Development Team'),
    ('Management', 'Management'),
    ('Supplier', 'Supplier'),
    ('Colleague for review', 'Colleague for review'),
    ('Unassigned', 'Unassigned'),
    
    )

    colleague = models.ForeignKey(Colleague, null=True, on_delete=models.CASCADE)
    incident = models.CharField(max_length=100, null=True) #incident number ...blank=true means don't need to complete
    title = models.CharField(max_length=100, null=True)
    summary = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100, choices=CATEGORY)
    status = models.CharField(max_length=100, choices=STATUS, null=True)
    recreate = models.TextField(max_length=300, null=True)
    date_raised = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now_add=True)
    priority =  models.CharField(max_length=25, choices=PRIORITY,null=True)
    assignee_team = models.CharField(max_length=100, choices=TEAM, null=True)
    escalated = models.BooleanField(default=False)

    #generates random incident number
    def save(self, *args, **kwargs):
        if not self.incident:
            # Generate a unique incident number
            while True:
                incident_number = 'INC' + get_random_string(length=7, allowed_chars='0123456789')
                if not Ticket.objects.filter(incident=incident_number).exists():
                    self.incident = incident_number
                    break
        super().save(*args, **kwargs)



    # ...
