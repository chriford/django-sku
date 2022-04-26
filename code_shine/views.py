from django.shortcuts import render, HttpResponse
from django.views.generic import ListView

class HomePage(ListView):
    template_name = 'index.html'
    
    def get_context_data(self, *args, **kwargs):
        
        context = super(HomePage, self).get_context_data(*args, **kwargs)
        context['greet'] = "Hello world!"
        return context
    
    def get_queryset(self):
        data = [1,2,3,4]
        return HttpResponse(f"{data}")


# Create your views here.
