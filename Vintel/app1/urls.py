from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.registerPage, name="registerPage"),
    path('login/', views.loginPage, name="loginPage"),
    path('logout/', views.logoutUser, name="logout"),
]