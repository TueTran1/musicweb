from dataclasses import field, fields
from pyexpat import model
import django
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Upload_Composer, Upload_Singer, Upload_Songs
from django import forms


class register_Form(UserCreationForm):
    class Meta:
        model = User
        fields =['username','password1','password2','last_name','first_name','email']

class changeUser_Form(ModelForm):
    class Meta:
        model = User
        fields =['username','last_name','first_name','email']

class addsong_Form(ModelForm):
    class Meta:
        model = Upload_Songs
        fields =['name','file','singer','composer','details']

class addcomposer_Form(ModelForm):
    class Meta:
        model = Upload_Composer
        fields =['name','real_name','image','details']

class addsinger_Form(ModelForm):
    class Meta:
        model = Upload_Singer
        fields =['name','real_name','image','details']



    