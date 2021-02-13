from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):
    posts = Post.objects
    return render(request, "index.html", {"posts" : posts})

def postDetail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "postDetail.html", {"post" : post})