from django.contrib import admin
from django.urls import path, include

from main import urls
from contact_app import urls
from auth import urls

from django.conf import settings
from django.conf.urls.static import static

from contact_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/profile/', views.dashboard, name="dashboard"),
    path('auth/', include('auth.urls')),
    path('contact_app/', include('contact_app.urls')),

    path('', include('main.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
