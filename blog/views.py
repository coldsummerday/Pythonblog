from django.shortcuts import render,get_object_or_404
from .models import Post,Category
import markdown
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger#主页分页用
from django.db.models import Q
def home(request):
    posts=Post.objects.all().order_by('-created_time')
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
    post.increase_views()
    md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
    post.body = md.convert(post.body)
    return render(request, 'blog/detail.html', context={'post': post,})

def archives(request,year,month):
    post_list=Post.objects.filter(created_time__year=year,created_time__month=month)
    return render(request,'blog/index.html',context={'post_list':post_list})

def category(request,pk):
    cate=get_object_or_404(Category,pk=pk)
    post_list=Post.objects.filter(category=cate)
    return render(request,'blog/index.html',context={'post_list':post_list})

def search(resuest):
    q=request.GET.get('q')
    error_msg=''
    if not q:
        error_msg="请输出关键词"
        return render(request, 'blog/index.html', {'error_msg': error_msg})
    post_list=Post.objects.filter(Q(title__icontains=q) | Q(body__icontains=q))
    return render(request,'blog/index.html', {'error_msg': error_msg,
                                               'post_list': post_list})
class PostDetailView(DetailView):
    # 这些属性的含义和 ListView 是一样的
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        response = super(PostDetailView, self).get(request, *args, **kwargs)
        self.object.increase_views()
        return response
    def get_object(self, queryset=None):
        post = super(PostDetailView, self).get_object(queryset=None)
        # 覆写 get_object 方法的目的是因为需要对 post 的 body 值进行渲染
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
        post.body = md.convert(post.body)
        post.toc = md.toc
        return post

