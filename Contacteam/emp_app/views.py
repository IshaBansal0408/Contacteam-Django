from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import render
from django.views.generic import (
    CreateView
)
from emp_app import models, forms
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
    success_url = ''

    def form_valid(self, form):
        form.instance.employer = self.request.user
        form.instance.hire_date = timezone.now()
        return super().form_valid(form)
