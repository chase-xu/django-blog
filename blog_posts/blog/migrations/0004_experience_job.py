# Generated by Django 4.1.2 on 2022-11-17 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_category_thumbnail_alter_post_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=225)),
                ('title', models.CharField(max_length=100)),
                ('years', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.TextField()),
                ('experience', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.experience')),
            ],
        ),
    ]
