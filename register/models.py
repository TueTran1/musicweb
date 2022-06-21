from django import forms
from django.db import models
from matplotlib import image, widgets
from numpy import real
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.


class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=30)
    name = models.TextField()
    birthday = models.DateField()
    details = models.TextField()

    def __str__(self):
        return self.username
def media_path(instance,filename):
    return '/'.join(['content',instance.user.id, filename])
class Upload_Singer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    real_name = models.CharField(max_length=255,null=True)
    image = models.ImageField(null=True,upload_to='media/')
    details = models.CharField(max_length=255,null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
        
class Upload_Composer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    real_name = models.CharField(max_length=255,null=True)
    image = models.ImageField(blank=True,upload_to='media/')
    details = models.CharField(max_length=255,null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Upload_Songs(models.Model):    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    file = models.FileField(blank=True)
    singer = models.ForeignKey("Upload_Singer", on_delete=models.CASCADE)  
    composer = models.ForeignKey("Upload_Composer", on_delete=models.CASCADE)   
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    details = models.CharField(max_length=255,null=True)
    
    def __str__(self):
        return self.name

