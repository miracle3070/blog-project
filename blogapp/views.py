from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.utils import timezone
from .models import Post, Comment
from .form import PostForm

def index(request):
    posts_list = Post.objects.all()
    paginator = Paginator(posts_list, 1)
    page = request.GET.get("page")
    posts = paginator.get_page(page)
    return render(request, "index.html", {"posts" : posts})

def postDetail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    try:
        comments = Comment.objects.filter(post_id=post_id)
        try:
            comments = comments.objects.all()
        except AttributeError:
            pass
    except Comment.DoesNotExist:
        comments = None

    return render(request, "postDetail.html", {"post" : post, "comments" : comments})

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

def comment(request):
    if request.method == "POST":
        pub_date = timezone.now()
        post_id = request.POST["post_id"]
        post = get_object_or_404(Post, pk=post_id)
        author = request.POST["author"]
        content = request.POST["content"]
        comment = Comment(author=author, pub_date=pub_date, content=content, post_id=post)
        comment.save()
        
        post_id = request.POST["post_id"]
        post = get_object_or_404(Post, pk=post_id)
        return redirect("postDetail", post_id=post_id)
    
    else:
        redirect("index")