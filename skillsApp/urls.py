from django.contrib import admin 
from django.urls import path
from skillsApp import views

urlpatterns = [
    path("", views.home, name='home'),
]