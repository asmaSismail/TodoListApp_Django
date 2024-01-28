from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms


class RegistrationForm (UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','id':'userName','label' : 'userName', 'placeholder':'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Valid Email is required'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'id':'pwd','label' : 'password','placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}))
    class Meta:
        model = get_user_model()
        fields = ('username','email','password1', 'password2')
        
class LoginForm(AuthenticationForm):
   username = forms.CharField(widget=forms.TextInput(attrs={'autofocus':True, 'id':'userName','label' : 'userName','placeholder':'Username Here', 'class':'form-control'}))
   password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'id':'pwd','label' : 'password','placeholder':'********'}))
