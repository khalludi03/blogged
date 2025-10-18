from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm
from .models import Post
# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request,'blog/index.html' , {'posts':posts})

def detail(request,slug):
    post = get_object_or_404(Post,slug=slug)
    if(request.method == 'POST'):
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('detail', slug=slug)
    else:
        form = CommentForm()    

    return render (request,'blog/detail.html', {'post':post, 'form': form})

def contact(request):
    return render(request, 'blog/contact.html')
