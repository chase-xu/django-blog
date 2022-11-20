from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    github = models.CharField(max_length=225)
    url = models.CharField(max_length=225)

    def __str__(self):
        return self.name