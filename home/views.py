from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
# Create your views here.
def index(request):
    return render(request, 'home/index.html')
