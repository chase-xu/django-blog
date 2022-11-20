from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Experience(models.Model):
    company = models.CharField(max_length=225)
    title = models.CharField(max_length=100)
    start_date = models.DateField(default=None, null=True)
    end_date = models.DateField(default=None, null=True)
    duty = models.TextField(null=True)

    def __str__(self):
        return self.company


class Job(models.Model):
    job = models.TextField()
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)

    def __str__(self):
        return self.job


class School(models.Model):
    name = models.CharField(max_length=100)
    degree = models.CharField(max_length=225)
    start_date = models.DateField(default=None, null=True)
    end_date = models.DateField(default=None, null=True)
    logo = models.ImageField(default=None, null=True)

    def __str__(self):
        return self.name