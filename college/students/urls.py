from django.urls import path

from . import views

urlpatterns = [
    path('',views.records_view,name='records_view')
]