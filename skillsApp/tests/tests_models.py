from django.test import TestCase
#imports for microsoft project test demo
from django.utils import timezone
from skillsApp.models import *
import datetime
###



# Create your tests here.


#Class is the blueprint(template), create an instance in memory from the blueprint with contains data
class LogMessageTests(TestCase):
    #create an LogMessage instance
    def create_LogMessage(self):
        #constructor = is the thing that runs to build the instance of the class 
        return LogMessage.objects.create(
             message="This is a test message",log_date = timezone.now())

    #create test instance of logmessage
    def test_logmessage_creation(self):
        '''
        test the creation of the log message instance, does it actually creates an instance
        '''
        log_message = self.create_LogMessage #ACT
        self.assertTrue(isinstance(log_message, LogMessage))#ASSERT

#ARRANGE

#ACT

#ASSERT