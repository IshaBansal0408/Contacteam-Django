from django.urls import path
from contact_app import views
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('addContact/', views.addContact.as_view(), name='addContact')
]
