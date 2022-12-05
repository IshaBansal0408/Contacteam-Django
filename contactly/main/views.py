from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    # return HttpResponse("Hello to Home Page")
    context = {}
    return render(request, 'main/home.html', context)
