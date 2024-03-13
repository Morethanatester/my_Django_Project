from django.contrib import admin 
from django.urls import path
from skillsApp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name='home'),
    path("home/", views.home, name='home'),
    path('user/', views.userPage, name="user-page"),
    path('faults/', views.faults, name = "faults"),
    path('settings/', views.settings, name="settings"),
    
    
    path('login/', views.loginPage, name = "login"),
    path('register/', views.registerPage, name = "register"),
    path('logout/', views.logoutUser, name = "logout"),

    path('colleagues/<str:pk>/', views.colleagues, name="colleagues"), #pk from view.py colleagues

    #CRUD Functionality

    path('create_ticket/', views.createTicket, name = "create_ticket"),
    path('create_ticket/<str:colleague_id>/', views.createTicket, name='create_ticket_for_colleague'),
    path('update_ticket/<str:pk>/', views.updateTicket, name = "update_ticket"),
    path('delete_ticket/<str:pk>/', views.deleteTicket, name = "delete_ticket"),




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
    



]


'''