from django.urls import path
from auth import views
urlpatterns = [
    path('signup/', views.signup, name='signup')
]
