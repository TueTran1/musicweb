from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from register.models import Upload_Singer

# Create your views here.
def index(request):
    upload_singer = Upload_Singer.objects.all() 
    return render(request, 'singers/singers.html', {'upload_singer': upload_singer})
