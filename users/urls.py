from django.urls import path
from django.contrib import admin
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.Login_View.as_view(), name='login'),
    path('logout/', views.Logout_View.as_view(), name='logout'),
    path('register/', views.Register.as_view(), name='register'),
]