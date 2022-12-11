from django.urls import path
from emp_app import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('addEmp', views.addEmp.as_view(), name='addEmp'),
    path('allEmp', views.allEmp.as_view(), name='allEmp'),
    path('partEmp', views.partEmp, name="partEmp"),
    path('delEmp/<int:pk>', views.delEmp.as_view(), name='delEmp'),
    path('updEmp/<int:pk>', views.updEmp.as_view(), name='updEmp'),
    path('viewEmp/<int:pk>', views.viewEmp.as_view(), name='viewEmp'),

    path('addDept', views.addDept.as_view(), name='addDept'),
    path('allDept', views.allDept.as_view(), name='allDept'),
    path('delDept/<int:pk>', views.delDept.as_view(), name='delDept'),
    path('updDept/<int:pk>', views.updDept.as_view(), name='updDept'),
    path('viewDept/<int:pk>', views.viewDept.as_view(), name='viewDept'),

]
