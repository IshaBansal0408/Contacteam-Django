from django.urls import path
from auth import views

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name="logout"),
    path('register/', views.addUser.as_view(), name='addUser')

]
