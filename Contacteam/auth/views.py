from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import (
    CreateView
)
from django.contrib.auth.views import (
    LoginView,
    LogoutView as Logout
)
from auth import forms
# Create your views here.


class Register(CreateView):
    model = User
    template_name = 'auth/signup.html'
    form_class = forms.addUser
    # fields = ['first_name', 'last_name', 'username', 'password']
    success_url = 'http://localhost:8000/'


class Login(LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True
