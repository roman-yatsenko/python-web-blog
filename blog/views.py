from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Post


def post_list(request):
    post_list = Post.published.all()
    # Посторінкове розбиття з 3 постами на сторінку
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status=Post.Status.PUBLISHED)
    
    return render(request, 'blog/post/detail.html', {'post': post})
