from django.contrib import admin
from django.urls import path, include
from emp_app import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('emp_app.urls'))
]
