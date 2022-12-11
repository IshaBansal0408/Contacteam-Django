from django.contrib import admin
from django.urls import path, include
from emp_app import urls
from auth import urls
from emp_app import views
urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('auth/', include('auth.urls')),
    path('accounts/profile/', views.dashboard, name='dashboard'),
    path('', include('emp_app.urls'))
]
