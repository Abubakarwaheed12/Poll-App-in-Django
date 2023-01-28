from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class userRoles(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE, related_name="role")
    is_teacher=models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} -  {self.is_teacher}'

