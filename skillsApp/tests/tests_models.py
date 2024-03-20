from django.test import TestCase
#imports for microsoft project test demo
from skillsApp.models import *
from skillsApp.forms import *
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
import uuid
from django.db import DatabaseError
from django.urls import reverse
###



# Create your tests here.


#failing test case to test pipeline
        

class SimpleTestCase(TestCase):
    def test_always_fails(self):
        self.assertEqual(1, 2, "This test always fails because 1 is not equal to 2")



class SecurityTest(TestCase):
    # This setup method is run before each test. It sets up a client for making requests and a test user.
    def setUp(self):
        # Arrange: Set up a client for making requests
        self.client = Client()

        # Arrange: Create a test user
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpass123'
        )

        # Arrange: Create a colleague for the test user
        self.colleague = Colleague.objects.create(
            user=self.user,
            first_name='Test',
            last_name='User',
            email='testuser@example.com',
            colleagueID='testuser123'
        )

    # This test checks that a CSRF token is included in the register page.
    def test_csrf(self):
        # Act: Make a GET request to the register page
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpass'}, csrf_using=False)

        # Assert: Check that the response contains a CSRF token
        self.assertContains(response, 'csrfmiddlewaretoken')

        # This test checks for SQL Injection vulnerability in the login page.
    def test_sql_injection(self):
        # Act: Make a POST request to the login page with a malicious username
        response = self.client.post(reverse('login'), {'username': "testuser'; DROP TABLE auth_user; --", 'password': 'testpass'})
        # Assert: Check that the response does not contain an OperationalError, which would indicate a SQL Injection vulnerability
        self.assertNotIn("OperationalError", response.content.decode())

    # This test checks for XSS vulnerability in the login page.
    def test_xss(self):
        # Act: Make a POST request to the login page with a malicious username
        response = self.client.post(reverse('login'), {'username': '<script>alert("XSS")</script>', 'password': 'testpass'})
        # Assert: Check that the response does not contain the malicious script, which would indicate an XSS vulnerability
        self.assertNotIn('<script>alert("XSS")</script>', response.content.decode())

    # This test checks for Sensitive Data Exposure in the login page.
    def test_sensitive_data_exposure(self):
        # Act: Make a GET request to the login page
        response = self.client.get(reverse('login'))
        # Assert: Check that the response does not contain the test user's password, which would indicate Sensitive Data Exposure
        self.assertNotIn('testpass123', response.content.decode())