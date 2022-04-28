from django.shortcuts import render
from django.contrib.auth.models import Permission, PermissionsMixin
from django.views.generic import ListView

class AnswerListView(ListView, PermissionsMixin):
    template_name = "answers.html"
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "answers"
        
    def get_queryset(self):
        return HttpResponse("Answers")

