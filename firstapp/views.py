from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'app/posts.html', {'posts': posts})


def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'app/post.html', {'post': post})