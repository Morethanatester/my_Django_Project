from django.db import models
from django.contrib.auth.models import User # django user model

# Create your models here.


class Colleague(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True) #null=True removes the need to complete all fields, TODO remove this and set default fields
    email = models.CharField(max_length=100, null=True)
    tel = models.CharField(max_length=100, null=True)
    colleagueID = models.CharField(max_length=8, null=True)
    jobfamily = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Keyword(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


        
class Ticket(models.Model):

    #DEFINE DROP DOWNS
    CATEGORY = (
        ('Equipment', 'Equipment'),
        ('Software', 'Software'),
        #TODO add more
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
        ('Resolution', 'Resolution'),
        ('Resolved','Resolved'),
    )
    
    incident = models.CharField(max_length=100, null=True) #incident number ...blank=true means don't need to complete
    colleague = models.ForeignKey(Colleague, null=True, on_delete=models.SET_NULL) #sets Colleague as parent model for colleague attribute in Ticket model #creates many to one relationship Colleague with Fault (one colleague can have many faults, faults can only have one collegaue)
    title = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100, choices=CATEGORY) #referance CATEGORY DROP DOWN OPTIONS...
    description = models.CharField(max_length=350, blank=True) #shirt description
    date_raised = models.DateTimeField(auto_now_add=True)
    priority =  models.CharField(max_length=100, choices=PRIORITY,null=True) #TODO, remove max_length? because it's a drop down
    assignee = models.CharField(max_length=100, choices=RESOLVERS, null=True)
    status = models.CharField(max_length=100, choices=STATUS, null=True)
    keyword = models.ManyToManyField(Keyword) #creates many to many relationship between Fault Class and Tag

    def __str__(self):
        #name = Colleague.firstname + " " + Colleague.sirname #TODO, trying to add both names, and returned in admin panel
        return self.title
