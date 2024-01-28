from django.contrib import admin
from django.urls import path,include
import users ,todoListApp

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include('users.urls', namespace = 'users')),
    path(r'', include('todoListApp.urls', namespace = 'todoListApp')),

]


