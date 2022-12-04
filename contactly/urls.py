from django.contrib import admin
from django.urls import path, include

from main import urls
from contact_app import urls
from auth import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth.urls')),
    path('contact_app/', include('contact_app.urls')),
    path('', include('main.urls'))
]
