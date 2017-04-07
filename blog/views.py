from django.shortcuts import render,get_object_or_404
from .models import Post,Category
import markdown
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger#主页分页用

def home(request):
    posts=Post.objects.all()
    paginator=Paginator(posts,5)
    page=request.GET.get('page')
    try:
        post_list=paginator.page(page)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.paginator(paginator.num_pages)
    return render(request,'blog/home.html',context={'post_list':post_list})

def index(request):
    post_list=Post.objects.all()
    return  render(request,'blog/index.html',context={'post_list':post_list})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(request, 'blog/detail.html', context={'post': post})

def archives(request,year,month):
    post_list=Post.objects.filter(created_time__year=year,created_time__month=month)
    return render(request,'blog/index.html',context={'post_list':post_list})

def category(request,pk):
    cate=get_object_or_404(Category,pk=pk)
    post_list=Post.objects.filter(category=cate)
    return render(request,'blog/index.html',context={'post_list':post_list})
