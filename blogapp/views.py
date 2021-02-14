from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post

def index(request):
    posts_list = Post.objects.all()
    paginator = Paginator(posts_list, 1)
    page = request.GET.get("page")
    posts = paginator.get_page(page)
    return render(request, "index.html", {"posts" : posts})

def postDetail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "postDetail.html", {"post" : post})