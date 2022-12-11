# from django_filters.views import FilterView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import render
from django.views.generic import (
    CreateView,
    ListView,
    DeleteView,
    UpdateView,
    DetailView
)
from emp_app import models, forms
from django.urls import reverse
from django.contrib.auth.models import User
# Create your views here.


def homePage(request):
    context = {}
    return render(request, 'emp_app/home.html', context)


@login_required(login_url='auth/login')
def dashboard(request):
    context = {
        'user': str(request.user)
    }
    print(str(request.user))
    return render(request, 'emp_app/dashboard.html', context)


class addEmp(LoginRequiredMixin, CreateView):
    model = models.Employee
    template_name = 'emp_app/addEmp.html'
    form_class = forms.addEmpForm
    success_url = 'allEmp'

    def form_valid(self, form):
        form.instance.employer = self.request.user
        form.instance.hire_date = timezone.now()
        return super().form_valid(form)


class allEmp(LoginRequiredMixin, ListView):
    model = models.Employee
    template_name = 'emp_app/allEmp.html'
    context_object_name = 'allEmpList'


def partEmp(request):
    allEmpList = models.Employee.objects.filter(employer=request.user)
    print(allEmpList)
    context = {
        'allEmpList': allEmpList
    }
    return render(request, 'emp_app/partEmp.html', context)


class delEmp(LoginRequiredMixin, DeleteView):
    model = models.Employee
    template_name = 'emp_app/delEmp.html'
    success_url = 'http://localhost:8000/allEmp'


class updEmp(LoginRequiredMixin, UpdateView):
    model = models.Employee
    template_name = 'emp_app/updEmp.html'
    form_class = forms.addEmpForm
    success_url = 'http://localhost:8000/allEmp'

    def form_valid(self, form):
        form.instance.employer = self.request.user
        form.instance.hire_date = timezone.now()
        return super().form_valid(form)


class viewEmp(LoginRequiredMixin, DetailView):
    model = models.Employee
    template_name = 'emp_app/viewEmp.html'


class addDept(LoginRequiredMixin, CreateView):
    model = models.Department
    template_name = 'emp_app/addDept.html'
    form_class = forms.addDeptForm
    success_url = 'allDept'


class allDept(LoginRequiredMixin, ListView):
    model = models.Department
    template_name = 'emp_app/allDept.html'
    context_object_name = 'allDeptList'


class delDept(LoginRequiredMixin, DeleteView):
    model = models.Department
    template_name = 'emp_app/delDept.html'
    success_url = 'http://localhost:8000/allEmp'


class updDept(LoginRequiredMixin, UpdateView):
    model = models.Department
    template_name = 'emp_app/updDept.html'
    form_class = forms.addDeptForm
    success_url = 'http://localhost:8000/allDept'


class viewDept(DetailView):
    model = models.Department
    template_name = 'emp_app/viewDept.html'
