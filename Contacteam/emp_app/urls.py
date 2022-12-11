from django.urls import path
from emp_app import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('addEmp', views.addEmp.as_view(), name='addEmp'),
    path('allEmp', views.allEmp.as_view(), name='allEmp'),
    path('delEmp/<int:pk>', views.delEmp.as_view(), name='delEmp'),
    path('updEmp/<int:pk>', views.updEmp.as_view(), name='updEmp'),
    path('viewEmp/<int:pk>', views.viewEmp.as_view(), name='viewEmp')
]
