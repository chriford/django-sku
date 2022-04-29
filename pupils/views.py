from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from .models import Question
from .forms import QuestionForm

class QuestionListView(LoginRequiredMixin, ListView):
    template_name = "questions.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "questions"
        context["form"] = QuestionForm()
        
        return context
    
    def get_queryset(self):
        return HttpResponse("Hello")


class UserQuestionListView(LoginRequiredMixin, ListView):
    template_name = "user_questions.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "questions"
        context["form"] = QuestionForm()
        
        return context
    
    def get_queryset(self):
        return HttpResponse("Hello")
