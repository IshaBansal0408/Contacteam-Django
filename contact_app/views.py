from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    CreateView
)
from contact_app import models
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


@login_required(login_url='http://localhost:8000/auth/login')
def dashboard(request):
    context = {
        'user': request.user
    }
    return render(request, 'contact_app/dashboard.html', context)


class addContact(LoginRequiredMixin, CreateView):
    model = models.Contact
    fields = '__all__'
    template_name = 'contact_app/addContact.html'
    success_url = 'allcontacts'
