from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.models import PermissionsMixin
# from .models import Question

class QuestionListView(ListView, PermissionsMixin):
    template_name = ""
    
    def get_context_data(self):
        context = super(self, QuestionListView).get_context_data()
        
        context["title"] = "questions"
        
        

# Create your views here.
