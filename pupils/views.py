from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.models import PermissionsMixin
from django.http import HttpResponse
# from .models import Question

class QuestionListView(ListView, PermissionsMixin):
    template_name = "questions.html"
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "questions"
        
    def get_queryset(self):
        return HttpResponse("Hello")
