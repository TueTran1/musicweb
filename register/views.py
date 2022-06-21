import email
from random import randint
from pathlib import Path
from django.core.files import File
from click import password_option
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.contrib import messages
from flask import current_app
from sklearn import compose
from .models import Upload_Singer, Upload_Songs
from register.models import Upload_Singer, Upload_Songs, Upload_Composer
from .forms import addcomposer_Form, register_Form,  changeUser_Form,addsinger_Form,addsong_Form
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_user(request):
    if request.method =="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = authenticate(request,username=User.objects.get(username=email),password=password)
        except:
            user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return render(request,"register/private.html")
        else:
            messages.success(request,'Đăng nhập thất bại!')
            return render(request, "register/login.html")
    return render(request, "register/login.html",{})


def register(request):
    form = register_Form()
    if request.method =="POST":
        form = register_Form(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Tài khoản '+ user +' đăng ký thành công !')
            return render(request, 'register/register.html')
    
    context = {'form':form}
    return render(request, 'register/register.html',context)
    
def random():
    value = randint(1,9999999)
    return value

@login_required(login_url='/register/login/')
def delete_song(request,event_id):
    current_user = request.user
    event = Upload_Songs.objects.get(id=event_id)
    event.delete()
    upload_songs= Upload_Songs.objects.all().filter(user=current_user)
    return render(request, 'register/private_song.html',{'upload_song': upload_songs})

@login_required(login_url='/register/login/')
def delete_singer(request,event_id):
    current_user = request.user
    event = Upload_Singer.objects.get(id=event_id)
    event.delete()
    upload_singer=Upload_Singer.objects.all().filter(user=current_user)
    return render(request, 'register/private_singer.html',{'upload_singer': upload_singer})
    
@login_required(login_url='/register/login/')
def delete_composer(request,event_id):
    current_user = request.user
    event = Upload_Composer.objects.get(id=event_id)
    event.delete()
    upload_composer=Upload_Composer.objects.all().filter(user=current_user)
    return render(request, 'register/private_composer.html',{'upload_composer': upload_composer})

@login_required(login_url='/register/login/')
def change_user(request):
    if request.method =="POST":
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        current_user = request.user
        b = User.objects.get(id=current_user.id)
        User.objects.all().update(first_name=first_name, last_name=last_name, email=email)
        if b is not None:
            messages.success(request,'Thay đổi thông tin thành công!')
            return render(request,"register/change_user.html")
        else:
            messages.success(request,'Thay đổi thông tin thất bại!')
            return render(request, "register/change_user.html")
    return render(request, "register/change_user.html")

@login_required(login_url='/register/login/')
def add_composer(request):
    if request.method =="POST":
        name = request.POST.get("name")
        real_name = request.POST.get("real_name")
        details = request.POST.get("details")
        image = request.FILES['image']
        id=random()
        current_user = request.user
        composer = Upload_Composer(id=id,name=name,image=image,real_name=real_name,details=details,user=current_user)
        if composer is not None:
            composer.save()
            messages.success(request,'Thêm nhạc sĩ ' +name+' thành công!')
            return render(request,"register/add_composer.html")
        else:
            messages.success(request,'Thêm nhạc sĩ thất bại!')
            return render(request, "register/add_composer.html")
    return render(request, "register/add_composer.html")

@login_required(login_url='/register/login/')
def add_singer(request):
    if request.method =="POST":
        name = request.POST.get("name")
        real_name = request.POST.get("real_name")
        image = request.FILES['image']
        details = request.POST.get("details")
        id=random()
        current_user = request.user
        singer = Upload_Singer(id=id,name=name,real_name=real_name,image=image,details=details,user=current_user)
        if singer is not None:
            singer.save()
            messages.success(request,'Thêm ca sĩ ' +name+' thành công!')
            return render(request,"register/add_singer.html")
        else:
            messages.success(request,'Thêm ca sĩ ' +name+' thất bại!')
            return render(request, "register/add_singer.html")
    return render(request, "register/add_singer.html")

@login_required(login_url='/register/login/')
def add_song(request):
    list_composer = Upload_Composer.objects.all()
    list_singer = Upload_Singer.objects.all()
    if request.method =="POST":
        name = request.POST.get("name")
        file = request.FILES['file']
        singer = request.POST.get("singer")
        composer = request.POST.get("composer")
        details = request.POST.get("details")
        upsinger = Upload_Singer.objects.get(id=singer)
        upcomposer = Upload_Composer.objects.get(id=composer)
        current_user = request.user
        id =random()
        song = Upload_Songs.objects.create(id=random(),name=name,file=file,singer=upsinger,composer=upcomposer,details=details,user=current_user)
        if song is not None:
            messages.success(request,'Thêm bài hát ' +name+' thành công!')
            return render(request,"register/add_song.html")
        else:
            messages.success(request,'Thêm bài hát ' +name+' thất bại!')
            return render(request, "register/add_song.html")
    return render(request, "register/add_song.html",{'list_composer':list_composer, 'list_singer': list_singer})

@login_required(login_url='/register/login/')
def logout_user(request):
    logout(request)
    return render(request, 'home/index.html')

class private(LoginRequiredMixin, View):
    login_url = '/'
    def get(self, request):
        current_user = request.user
        return render(request, 'register/private.html',{'current_user': current_user})

class private_song(LoginRequiredMixin, View):
    login_url = '/'

    def get(self, request):
        current_user = request.user
        upload_song = Upload_Songs.objects.all().filter(user=current_user)
        return render(request, 'register/private_song.html',{'upload_song': upload_song})

class private_singer(LoginRequiredMixin, View):
    login_url = '/'
    def get(self, request):
        current_user = request.user
        upload_singer = Upload_Singer.objects.all().filter(user=current_user)
        return render(request, 'register/private_singer.html',{'upload_singer': upload_singer})

class private_composer(LoginRequiredMixin, View):
    login_url = '/'

    def get(self, request):
        current_user = request.user
        upload_composer = Upload_Composer.objects.all().filter(user=current_user)
        return render(request, 'register/private_composer.html',{'upload_composer': upload_composer})


