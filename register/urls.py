from tkinter import N
from . import views
from django.urls import include, path
from django.conf import settings
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
app_name = 'register'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('private/', views.private.as_view(), name='private'),
    path('song/', views.private_song.as_view(), name='private_song'),
    path('composer/', views.private_composer.as_view(), name='private_composer'),
    path('singer/', views.private_singer.as_view(), name='private_singer'),
    path('add_composer/', views.add_composer, name='add_composer'),
    path('add_singer/', views.add_singer, name='add_singer'),
    path('add_song/', views.add_song, name='add_song'),
    #path('forgetpassword/', views.forgetpassword(), name='forgetpassword')
    path('change_user/', views.change_user, name='change_user'),
    path('newpassword/', auth_views.PasswordChangeView.as_view(template_name='register/newpassword.html',success_url='login'), name = 'newpassword'),
    path('newpassword/login/', views.login_user, name='newpassword_success'),
    path('delete_song/<event_id>',views.delete_song,name='delete_song'),
    path('delete_singer/<event_id>',views.delete_singer,name='delete_singer'),
    path('delete_composer/<event_id>',views.delete_composer,name='delete_composer'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
