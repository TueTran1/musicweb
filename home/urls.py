from tkinter import N
from . import views
from django.urls import include, path
app_name = 'home'
urlpatterns = [
    path('', views.index, name='home')
]
