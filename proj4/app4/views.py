from os import name
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request): 
    context_dict = {'text':'hello world hellos prameet','number':100}
    return render(request,'app4/index.html',context=context_dict)

def other(request):
    return render(request,'app4/other.html')

def relative(request):
    return render(request,'app4/relative_url_templates.html')