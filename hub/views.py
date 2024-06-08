from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .forms import Signup

user = get_user_model


# Create your views here.
def HomePageView(request):
    return render(request, "index.html")


def LoginView(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        log = authenticate(request, username=username, password=password)
        if log is not None:
            login(request, log)
            return redirect("home")
    return render(request, "login.html")


def SignupView(request):
    if request.method == "POST":
        form = Signup(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = Signup()
    return render(request, "signup.html", {"form": form})


class ProfileView(DetailView):
    model=User
    template_name="Profile.html"


def PickupView(request):
    return render(request, "pickup.html")


def Logout(request):
    logout(request)
    return redirect("login")
