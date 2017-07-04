from django import  template
from ..models import Post,Category

register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    postlist=Post.objects.all().order_by('-created_time')[:num]
    return postlist

@register.simple_tag
def archives():
    return Post.objects.dates('created_time','month',order='DESC')

@register.simple_tag
def get_categories():
    return Category.objects.all()
