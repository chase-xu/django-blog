# Generated by Django 4.1.2 on 2022-11-22 06:57

from django.db import migrations, models
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_post_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('about', django_quill.fields.QuillField(null=True)),
            ],
        ),
    ]
