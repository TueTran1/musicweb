from tkinter import N
from . import views
from django.urls import include, path
app_name = 'composers'
urlpatterns = [
    path('', views.index, name='composers')
]
