from django.db import models
from django.conf import settings


class Student(models.Model):
    student_first_name = models.CharField(max_length=50)
    student_last_name = models.CharField(max_length=50)
    sex = models.BooleanField(null=True)
    CURP = models.CharField(max_length=22, null=True)
    birthday = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tutor_first_name = models.CharField(max_length=50)
    tutor_last_name = models.CharField(max_length=50)
    contact_cellphone = models.CharField(max_length=10)
    contact_telephone = models.CharField(max_length=10)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name="students")

    def __str__(self):
        return self.student_first_name + " " + self.student_last_name


class Ratings(models.Model):
    rating_1 = models.FloatField(default=0)
    rating_2 = models.FloatField(default=0)
    rating_3 = models.FloatField(default=0)
    rating_4 = models.FloatField(default=0)
    rating_5 = models.FloatField(default=0)
    rating_6 = models.FloatField(default=0)
    rating_7 = models.FloatField(default=0)
    rating_8 = models.FloatField(default=0)
    rating_9 = models.FloatField(default=0)
    rating_10 = models.FloatField(default=0)
    student = models.OneToOneField(Student,
                                   on_delete=models.CASCADE,
                                   related_name="ratings")
