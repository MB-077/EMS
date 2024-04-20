from django.db import models

# Create your models here.

class Student(models.Model):
    uid = models.CharField(primary_key=True, max_length=10)  # Assuming a maximum length of 10 characters for alphanumeric UID
    user_name = models.CharField(max_length=30)
    user_roll_no = models.CharField(max_length=30, unique=True)  # Assuming alphanumeric and unique roll numbers
    user_room_no = models.CharField(max_length=10)  # Assuming alphanumeric room numbers
    user_current_status = models.BooleanField(default=True)  # Assuming a boolean field for current status of student

    def __str__(self):
        return self.user_roll_no
    