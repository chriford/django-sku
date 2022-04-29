from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    render, 
    reverse,
    redirect,
    HttpResponse, 
    HttpResponseRedirect, 
)
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .models import User, UserProfile

def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, password=password, username=username)
        if user is not None:
            auth_login(request, user)
            return redirect("pupils:questions")
        else:
            messages.add_message(request, messages.ERROR, "wrong password or username")
            
    return render(request, "accounts/login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        users = [user.username, user.email not in User.objects.all()]
        if len(password1).__eq__(len(password2)) & username not in users & email not in users:
            new_user = User(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password1,
            )
            new_user.set_password(new_user.password)
            new_user.save()
        return redirect("/")
    
    return render(request, "accounts/register.html")


class SystemUsersListView(LoginRequiredMixin, ListView):
    template_name = "system-users.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "users"
        
        return context
    
    def get_queryset(self):
        return HttpResponse("...")


class HomeListView(LoginRequiredMixin, ListView):
    template_name = "home/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "home"
        return context
    
    def get_queryset(self):
        return HttpResponse("...")
