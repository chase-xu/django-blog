from django.urls import path
from . import views

urlpatterns = [
    path('/<int:postid>', views.post, name='post'),
    path('/category/<int:category>', views.category_post_list, name='category'),
]