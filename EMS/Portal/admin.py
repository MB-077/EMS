from django.contrib import admin

# Register your models here.

from .models import Room, User_Login, Student


admin.site.register(Room)
admin.site.register(User_Login)
admin.site.register(Student)
