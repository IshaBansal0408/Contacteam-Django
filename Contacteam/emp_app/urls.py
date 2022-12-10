from django.urls import path
from emp_app import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('addEmp', views.addEmp.as_view(), name='addEmp')
]
