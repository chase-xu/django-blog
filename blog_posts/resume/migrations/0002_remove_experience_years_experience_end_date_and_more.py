# Generated by Django 4.1.2 on 2022-11-17 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experience',
            name='years',
        ),
        migrations.AddField(
            model_name='experience',
            name='end_date',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='experience',
            name='start_date',
            field=models.DateField(default=None),
        ),
    ]
