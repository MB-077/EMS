from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *  # Assuming your models are defined here

@receiver(post_save, sender=Student)
def create_related_objects(sender, instance, created, **kwargs):
  if created:  # Check if object is newly created
    user_login = User_Login(student_roll_no=instance.student_roll_no, password=instance.student_roll_no)
    user_login.save()
    room = Room(uid=instance.student_roll_no, student=instance)
    room.save()