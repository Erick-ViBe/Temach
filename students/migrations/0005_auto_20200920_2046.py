# Generated by Django 3.1.1 on 2020-09-20 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20200920_2020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='rating_eight',
        ),
        migrations.RemoveField(
            model_name='student',
            name='rating_five',
        ),
        migrations.RemoveField(
            model_name='student',
            name='rating_four',
        ),
        migrations.RemoveField(
            model_name='student',
            name='rating_nine',
        ),
        migrations.RemoveField(
            model_name='student',
            name='rating_one',
        ),
        migrations.RemoveField(
            model_name='student',
            name='rating_seven',
        ),
        migrations.RemoveField(
            model_name='student',
            name='rating_six',
        ),
        migrations.RemoveField(
            model_name='student',
            name='rating_ten',
        ),
        migrations.RemoveField(
            model_name='student',
            name='rating_three',
        ),
        migrations.RemoveField(
            model_name='student',
            name='rating_two',
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_one', models.PositiveSmallIntegerField(default=0)),
                ('rating_two', models.PositiveSmallIntegerField(default=0)),
                ('rating_three', models.PositiveSmallIntegerField(default=0)),
                ('rating_four', models.PositiveSmallIntegerField(default=0)),
                ('rating_five', models.PositiveSmallIntegerField(default=0)),
                ('rating_six', models.PositiveSmallIntegerField(default=0)),
                ('rating_seven', models.PositiveSmallIntegerField(default=0)),
                ('rating_eight', models.PositiveSmallIntegerField(default=0)),
                ('rating_nine', models.PositiveSmallIntegerField(default=0)),
                ('rating_ten', models.PositiveSmallIntegerField(default=0)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='students.student')),
            ],
        ),
    ]
