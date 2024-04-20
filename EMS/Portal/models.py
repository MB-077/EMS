from django.db import models

class Student(models.Model):
    student_roll_no = models.CharField(max_length=30, unique=True, primary_key=True)
    student_name = models.CharField(max_length=30, null=True)
    student_room_no = models.CharField(max_length=10, null=True)
    student_hostel_status = models.BooleanField(default=True)
    student_hostel_out_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.student_roll_no}, Room: {self.student_room_no}"

    def save(self, *args, **kwargs):
        if not self.pk:  # Only execute if the object is being created (not updated)
            user_login = User_Login(student_roll_no=self.student_roll_no, password=self.student_roll_no)
            user_login.save()  # Save the User_Login object
            room = Room(uid=self.student_roll_no, student=self)
            room.save()
        super().save(*args, **kwargs)

class Room(models.Model):
    uid = models.CharField(max_length=10, unique=True, primary_key=True)
    room_light_status = models.BooleanField(default=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f"Room: {self.student.student_room_no}, Assigned Student: {self.student.student_name}"


class User_Login(models.Model):
    student_roll_no = models.CharField(max_length=30, unique=True, primary_key=True)
    password = models.CharField(max_length=30)  # Storing passwords in plaintext
    remember_me = models.BooleanField(default=False)

    def __str__(self):
        return self.student_roll_no