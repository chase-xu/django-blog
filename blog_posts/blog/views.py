from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Post, Category, Author
from django.core.paginator import Paginator
# Create your views here.

def homepage(request):
    featured = Post.objects.filter(featured=True).order_by('-timestamp')
    # latest = Post.objects.order_by('-timestamp')[0:3]
    context = {
        'object_list': featured,
        # 'latest': latest,
    }
    return render(request, 'homepage.html', context)

def post(request, postid=1):
    post = Post.objects.get(id=postid)
    context = {
        'post': post,
    }
    return render(request, 'post.html', context)

def about(request):
    return render(request, 'about_page.html')

def category_post_list (request, slug):
    category = Category.objects.get(slug=slug)
    posts = Post.objects.filter(categories__in=[category])
    context = {
        'posts': posts
    }
    return render(request, 'post_list.html', context)

def allposts(request, page=1):
    posts = Post.objects.order_by('-timestamp')
    categories = Post.categories
    # paginator= Paginator(posts, per_page=6)
    # page_object = paginator.get_page(page)
    context = {
        'posts': posts,
        # 'page_object': page_object,
    }
    return render(request, 'all_posts.html', context)

def allposts_api(request):
    page_number = request.GET.get('page', 1)
    per_page = request.GET.get("per_page", 2)
    startswith = request.GET.get("startswith", "")
    keywords = Post.objects.filter(
        name__startswith=startswith
    )
    paginator = Paginator(keywords, per_page)
    page_obj = paginator.get_page(page_number)
    data = [{"name": kw.name} for kw in page_obj.object_list]

    payload = {
        "page": {
            "current": page_obj.number,
            "has_next": page_obj.has_next(),
            "has_previous": page_obj.has_previous(),
        },
        "data": data
    }
    return JsonResponse(payload)

