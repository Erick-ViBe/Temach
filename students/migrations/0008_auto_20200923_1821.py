# Generated by Django 3.1.1 on 2020-09-23 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_student_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='CURP',
            field=models.CharField(max_length=22, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='birthday',
            field=models.DateField(null=True),
        ),
    ]
