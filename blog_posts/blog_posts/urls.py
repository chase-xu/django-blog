"""blog_posts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from blog.views import homepage, post, about, category_post_list, allposts
from resume.views import resume
from projects.views import project

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings



urlpatterns = [
    path('', homepage, name = 'posts'),
    path('post/<int:postid>/', post, name='post'),
    path('post/category/<int:category>/', category_post_list, name='category'),
    path('posts/all/', allposts, name='allposts'),
    path('posts/featured/', homepage, name='posts'),
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path("resume/", resume, name='resume'),
    path('projects/', project, name='projects'),
    path('about/',  about, name='abouts',),
]
    
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)