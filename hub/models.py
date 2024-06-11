# models.py

from django.contrib.auth.models import AbstractUser,Group,Permission
from django.db import models


class Custom_User(AbstractUser):
    mobile = models.CharField(max_length=15, blank=True, null=True)
    groups = models.ManyToManyField(Group, related_name="customuser_set", blank=True)
    user_permissions = models.ManyToManyField(
        Permission, related_name="customuser_set", blank=True
    )

    def __str__(self):
        return self.username
class Map(models.Model):
    place=models.TextField(max_length="20")
    def __str__(self):
        return self.place
