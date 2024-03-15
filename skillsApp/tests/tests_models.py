from django.test import TestCase
#imports for microsoft project test demo
from django.utils import timezone
from skillsApp.models import *
from skillsApp.forms import *
import datetime
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
import uuid
from django.db import DatabaseError
###



# Create your tests here.


#failing test case to test pipeline
        
'''
class SimpleTestCase(TestCase):
    def test_always_fails(self):
        self.assertEqual(1, 2, "This test always fails because 1 is not equal to 2")
'''


'''
DEMO tests


#Class is the blueprint(template), create an instance in memory from the blueprint with contains data
class LogMessageTests(TestCase):
    #create an LogMessage instance
    def create_LogMessage(self):
        #constructor = is the thing that runs to build the instance of the class 
        return LogMessage.objects.create(
            message="This is a test message",
            log_date = timezone.now())

    #create test instance of logmessage
    def test_logmessage_creation(self):

        #test the creation of the log message instance, does it actually creates an instance

        log_message = self.create_LogMessage()  #Act
        self.assertTrue(isinstance(log_message, LogMessage))

'''

# This test case class contains tests related to security aspects of the application.
class SecurityTest(TestCase):

# This setup method is run before each test. It sets up a client for making requests and a test user.
    def setUp(self):
        self.client = Client() # Arrange
        self.user = get_user_model().objects.create_user( # Arrange
            username='testuser',
            password='testpass123'
        )
        self.colleague = Colleague.objects.create(
            user=self.user,
            first_name='Test',
            last_name='User',
            email='testuser@example.com',
            colleagueID='testuser123'
        )
# This test checks that a CSRF token is included in the register page.
    def test_csrf(self):
        response = self.client.get('/register/') # Act
        self.assertContains(response, 'csrfmiddlewaretoken') # Assert

# This test checks that sensitive data (the password) is not included in the response after logging in.
    def test_sensitive_data_exposure(self):
        response = self.client.post('/login/', { # Act
            'username': 'testuser',
            'password': 'testpass123'
        }, follow=True)
        self.assertNotContains(response, 'testpass123') # Assert