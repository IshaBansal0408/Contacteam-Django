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
    # fields = '__all__'
    form_class = forms.addEmpForm
    success_url = 'allEmp'

    def form_valid(self, form):
        form.instance.employer = self.request.user
        form.instance.hire_date = timezone.now()
        return super().form_valid(form)

    # def get_absolute_url(self):  # new
    #     return reverse('allEmp', args=[str(self.id)])


class allEmp(LoginRequiredMixin, ListView):
    model = models.Employee
    template_name = 'emp_app/allEmp.html'
    context_object_name = 'allEmpList'


class delEmp(LoginRequiredMixin, DeleteView):
    model = models.Employee
    template_name = 'emp_app/delEmp.html'
    success_url = 'http://localhost:8000/allEmp'


class updEmp(LoginRequiredMixin, UpdateView):
    # model = models.Employee
    # template_name = 'emp_app/updEmp.html'
    # context_object_name = 'empobj'

    model = models.Employee
    template_name = 'emp_app/updEmp.html'
    # fields = '__all__'
    form_class = forms.addEmpForm
    success_url = 'http://localhost:8000/allEmp'

    def form_valid(self, form):
        form.instance.employer = self.request.user
        form.instance.hire_date = timezone.now()
        return super().form_valid(form)


class viewEmp(DetailView):
    model = models.Employee
    template_name = 'emp_app/viewEmp.html'
