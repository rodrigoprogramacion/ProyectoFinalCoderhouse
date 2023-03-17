from django.shortcuts import render
from .models import Post

def blog(request):

    posts=Post.objects.all()
    return render(request, "AppBlog/blog.html",{"posts":posts})


# Create your views here.

