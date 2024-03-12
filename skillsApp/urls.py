from django.contrib import admin 
from django.urls import path
from skillsApp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name='home'),
    path("home/", views.home, name='home'),
    path('faults/', views.faults, name = "faults"),
    path('settings/', views.Settings, name="settings"),
    path('login/', views.loginPage, name = "login"),
    path('logout/', views.logoutUser, name = "logout"),

    #CRUD Functionality


#not sure these are working/functional

    #PASSWORD RESET URLS
    path('reset_password/',
    auth_views.PasswordResetView.as_view(template_name="skillsApp/password_reset.html"),
    name="reset_password"),
    
    path('reset_password_sent/', 
    auth_views.PasswordResetDoneView.as_view(template_name="skillsApp/password_reset_sent.html"), 
    name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name="skillsApp/password_reset_form.html"), 
    name="password_reset_confirm"),

    path('reset_password_complete/', 
    auth_views.PasswordResetCompleteView.as_view(template_name="skillsApp/password_reset_done.html"), 
    name="password_reset_complete"),

]





'''

urlpatterns = [
    path('user/', views.userPage, name="user-page"),
    path('colleagues/<str:pk>/', views.colleagues, name="colleagues"), #pk from view.py colleagues
    path('register/', views.registerPage, name = "register"),
    path('create_fault/<str:pk>/', views.createFault, name = "create_fault"), # HANDLES CREATE CRUD FUNCTION, PASSED INTO DASHBOARD HTML CREATE FAULT BUTTON
    path('update_fault/<str:pk>/', views.updateFault, name = "update_fault"),
    path('delete_fault/<str:pk>/', views.deleteFault, name = "delete_fault"),


]


'''