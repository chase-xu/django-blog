from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=20, null=True)
    slug = models.SlugField(null=True)
    thumbnail = models.ImageField(blank=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField(blank=True)
    categories = models.ManyToManyField(Category, related_name='Post')
    featured = models.BooleanField()

    def __str__(self):
        return self.title



