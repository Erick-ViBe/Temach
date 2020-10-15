from django.db import models
from django.contrib.auth.models import AbstractUser


class Teacher(AbstractUser):
    grade = models.PositiveSmallIntegerField(default=0)
    phone_number = models.CharField(max_length=10, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
