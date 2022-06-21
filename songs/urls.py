from django.conf.urls.static import static
from tkinter import N

from django.conf import settings
from . import views
from django.urls import include, path
app_name = 'songs'
urlpatterns = [
    path('', views.index, name='songs')
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
