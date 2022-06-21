from django.contrib import admin

# Register your models here.
from .models import Upload_Composer, Users,Upload_Singer, Upload_Songs
# Register your models here.
admin.site.register(Users)
admin.site.register(Upload_Singer)
admin.site.register(Upload_Composer)
admin.site.register(Upload_Songs)