from django.http import HttpResponse
from django.shortcuts import render

from register.models import Upload_Songs


# Create your views here.
def index(request):
    upload_song = Upload_Songs.objects.all()
    return render(request, 'songs/songs.html',{'upload_song': upload_song})
