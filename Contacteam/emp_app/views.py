from django.shortcuts import render

# Create your views here.


def homePage(request):
    context = {}
    return render(request, 'emp_app/home.html', context)


def dashboard(request):
    context = {}
    return render(request, 'emp_app/dashboard.html', context)
