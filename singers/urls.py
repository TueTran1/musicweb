from django.conf import settings
from django.conf.urls.static import static
from tkinter import N
from . import views
from django.urls import include, path
app_name = 'singers'
urlpatterns = [
    path('', views.index, name='singers'),
]
