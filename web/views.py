from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
from .models import *


def main_view(request):
    examples = User.objects.all()
    # examples = User.objects.filter(name__contains='bla')
    return render(request, 'web/index.html', {'examples': examples})


def add_view(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(data=request.POST, instance=None)
        if form.is_valid():
            form.save()
            return redirect('main')
    return render(request, 'web/form.html', {'form': form})


def delete_view(request, id):
    ex = get_object_or_404(User, id=id)
    ex.delete()
    return redirect('main')


def author_view(request, id):
    user = get_object_or_404(User, id=id)

    return render(request, 'web/author.html', {
        'user': user,
        'posts': user.post_set.all()
    })


def edit_view(request, id):
    user = get_object_or_404(User, id=id)
    form = UserForm(data=request.POST or None, instance=user)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('main')
    return render(request, 'web/form.html', {'form': form})


def add_post_view(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(data=request.POST, instance=None)
        if form.is_valid():
            form.save()
            return redirect('main')
    return render(request, 'web/form.html', {'form': form})


def posts_view(request):
    posts = Post.objects.all()
    return render(request, 'web/posts.html', {'posts': posts})


def post_view(request, id):
    # Post.objects.create(
    #     title='dadas',
    #     text='text',
    #     author=User.objects.create(
    #         name='dsada',
    #         age=15
    #     )
    # )
    post = get_object_or_404(Post, id=id)
    print(post.author.age)
    return render(request, 'web/post.html', {'post': post})
