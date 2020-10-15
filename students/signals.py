from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from students.models import Student, Ratings
from core.utils import generate_random_string


@receiver(post_save, sender=Student)
def create_ratings(sender, instance, created, **kwargs):
    if created:
        Ratings.objects.create(student=instance)


@receiver(pre_save, sender=Student)
def add_slug_to_student(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug1 = slugify(instance.student_first_name)
        slug2 = slugify(instance.student_last_name)
        random_string = generate_random_string()
        instance.slug = slug1 + "-" + slug2 + "-" + random_string
