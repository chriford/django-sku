from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import User, UserProfile
from django.contrib.auth.decorators import login_required


def login(request):
    return render("accounts/login.html")

def register(request):
    return render("accounts/register.html")
