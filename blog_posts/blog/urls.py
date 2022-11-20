from django.urls import path
from . import views

urlpatterns = [
    path('/<int:postid>', views.post, name='post'),
]