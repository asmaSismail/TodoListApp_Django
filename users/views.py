from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model
from .forms import LoginForm,RegistrationForm
from django.shortcuts import resolve_url
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View
from django.views.generic import CreateView
from django.urls import reverse_lazy

class Login_View(LoginView):

    model = get_user_model()
    form_class = LoginForm
    template_name = 'login.html'

    def get_success_url(self):
        url = resolve_url('todoListApp:tasks')
        return url


class Logout_View(View):

    def get(self,request):
        logout(self.request)
        return redirect ('users:login',permanent=True)
 

class Register (CreateView):
    model = get_user_model()
    form_class  = RegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('users:login')