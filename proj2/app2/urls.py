from django import urls
from . import views
from django.urls import include,path

urlpatterns = [
    path('',views.help,name='help')
]