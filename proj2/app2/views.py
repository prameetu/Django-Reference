from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def help(request):
    d = {'help_insert':'Help Page'}
    return render(request,'app2/help.html',context=d)