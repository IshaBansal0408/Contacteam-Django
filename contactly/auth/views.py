from django.shortcuts import render
from django.contrib.auth.views import (
    LoginView,
    LogoutView as Logout
)
from django.contrib.auth.models import User
from django.views.generic import (
    CreateView,
    ListView,
    DetailView
)

# Create your views here.


class Login(LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True
    success_url = 'http://localhost:8000/contact_app/'


class addUser(CreateView):
    model = User
    template_name = 'auth/addUser.html'
    # fields = '__all__'
    fields = ['first_name', 'last_name', 'username', 'password']
    success_url = 'http://localhost:8000/contact_app/'
