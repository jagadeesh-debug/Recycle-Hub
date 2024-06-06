from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.HomePageView, name="home"),
    path("login", views.LoginView, name="login"),
    path("signup", views.SignupView, name="signup"),
    path("pickup", views.PickupView, name="pickup"),
]
