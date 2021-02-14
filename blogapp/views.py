from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.utils import timezone
from .models import Post
from .form import PostForm

def index(request):
    posts_list = Post.objects.all()
    paginator = Paginator(posts_list, 1)
    page = request.GET.get("page")
    posts = paginator.get_page(page)
    return render(request, "index.html", {"posts" : posts})

def postDetail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "postDetail.html", {"post" : post})

def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.author = request.user.username
            post.save()
            return redirect("index")
    else:
        form = PostForm()
        return render(request, "create.html", {"form":form})