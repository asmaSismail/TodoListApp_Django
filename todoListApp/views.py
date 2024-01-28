from django.shortcuts import render
from .models import Task
from .forms import TaskForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import   CreateView,View,ListView,UpdateView
from django.shortcuts import redirect
from django.utils import timezone

class Tasks(LoginRequiredMixin,ListView):
   template_name = 'tasksList.html'
   model=Task
   login_url = 'users:login'
   context_object_name = 'tasks'
   def get_queryset(self):
      filters={}
      context = super().get_queryset()
      filters['user'] = self.request.user
      if self.request.GET.get("page")== None:
           for key, value in self.request.GET.items():
              print("hello world!")
              print(value)
              if value != '*' and value != '':
                filters[key] = value
           
           new_context = Task.objects.filter(
                   **filters
               )
           return new_context
         
      return context
      
   def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Tasks=Task.objects.all()
        return context

class Task_New(LoginRequiredMixin,CreateView):
    model = Task 
    form_class = TaskForm  
    template_name = 'taskEdit.html'
    login_url = 'users:login'
    success_url = reverse_lazy('todoListApp:tasks') 
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class Task_Update(LoginRequiredMixin,UpdateView):
    model = Task
    template_name = 'taskEdit.html'
    form_class = TaskForm
    login_url = 'users:login'
    success_url = reverse_lazy('todoListApp:tasks') 
    
class Task_Delete(LoginRequiredMixin,View):
    login_url = 'users:login'
    def get(self, request ,pk):
        emp = Task.objects.get(pk=pk)
        emp.delete()
        return redirect('todoListApp:tasks', permanent=True)
  
