from django.contrib import admin
from django.urls import path, include
from emp_app import urls
from auth import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth.urls')),
    path('', include('emp_app.urls'))
]
