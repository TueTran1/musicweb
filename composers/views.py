from django.shortcuts import render

from register.models import Upload_Composer

# Create your views here.
def index(request):
    upload_composer = Upload_Composer.objects.all() 
    return render(request, 'composers/composers.html', {'upload_composer': upload_composer})