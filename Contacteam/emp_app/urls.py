from django.urls import path
from emp_app import views

urlpatterns = [
    path('', views.homePage, name='home')
]
