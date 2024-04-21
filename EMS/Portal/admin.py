from django.contrib import admin
from .models import Room, User_Login, Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
  def save_model(self, request, obj, form, change):
    super().save_model(request, obj, form, change)
    if not change:  # Check if object is newly created
      user_login = User_Login(student_roll_no=obj.student_roll_no, password=obj.student_roll_no)
      user_login.save()
      room = Room(uid=obj.student_roll_no, student=obj)
      room.save()

admin.site.register(Student, StudentAdmin)
admin.site.register(Room)
admin.site.register(User_Login)
