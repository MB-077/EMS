from django.db import models

# Create your models here.

from django.db import models

class user_login(models.Model):
    user_roll_no = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    remember_me = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user_roll_no