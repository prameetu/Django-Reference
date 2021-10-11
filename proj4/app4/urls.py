from os import name
from django.urls import path

from app4 import views

app_name = 'app4'

urlpatterns = [
    path('other/', views.other, name='other'),
    path('relative/',views.relative,name='relative')

]