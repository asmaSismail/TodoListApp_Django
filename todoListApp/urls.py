from django.urls import path
from django.contrib import admin
from . import views

app_name = 'todoListApp'

urlpatterns = [
    path('tasks/', views.Tasks.as_view(), name='tasks'),
    path('tasks/<int:pk>/delete/', views.Task_Delete.as_view(), name='Task_delete'),
    path('tasks/<int:pk>/update/', views.Task_Update.as_view(), name='Task_update'),
    path('tasks/new/', views.Task_New.as_view(), name='Task_New'),
    ]