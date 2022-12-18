from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
import os, json

def ROOT():
    DATA = []
    for file in os.listdir(r"main/nft"):
        if file.endswith(".json"):
            DATA.append(json.load(open("main/nft/"+file, "r")))
            img = DATA[-1]["image"]
            DATA[-1]["image"] = "https://ipfs.io/ipfs/" + img.split('ipfs://')[1]
    return DATA

def index(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request=request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        messages.error(request, "Username or Password Not Correct")
        return redirect("index")
    return render(request, "index.html")

def register(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get("username")
            password = request.POST.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("dashboard")
        messages.error(request, "Unsuccessful")
        return redirect("register")
    DATA = {"form": UserCreationForm()}
    return render(request, "register.html", DATA)

@login_required(login_url="index")
def dashboard(request):
    DATA = {"user": request.user,
            "data": ROOT()}
    return render(request, "dashboard.html", DATA)

@login_required(login_url="index")
def user_logout(request):
    logout(request)
    return redirect("index")

