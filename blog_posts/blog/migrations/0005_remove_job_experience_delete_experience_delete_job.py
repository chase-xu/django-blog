# Generated by Django 4.1.2 on 2022-11-17 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_experience_job'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='experience',
        ),
        migrations.DeleteModel(
            name='Experience',
        ),
        migrations.DeleteModel(
            name='Job',
        ),
    ]