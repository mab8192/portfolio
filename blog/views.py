from django.shortcuts import render
from blog.models import Post, Comment

# Create your views here.
def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {'posts': posts}
    return render(request, 'blog_index.html', context)

def blog_detail(request, pk):
    pass

def blog_category(request, pk):
    pass
