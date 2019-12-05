from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from blog.models import Post
from.import forms

# Create your views here.

def post_list(request):
    post = Post.objects.all().order_by('dt_cri_post')
    return render(request, 'blog/post_list.html', {'post': post})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required(login_url="/autor/login/")
def post_create(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            # save post to db
            instance = form.save(commit=False)
            instance.autor = request.user
            instance.save()
            return redirect('blog:list')
    else:
        form = forms.CreatePost()
    return render(request, 'blog/post_create.html', {'form': form})