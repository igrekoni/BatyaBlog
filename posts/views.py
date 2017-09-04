from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404,redirect
from .models import Post
from .forms import PostForm


def mainpage(request):
    queryset = Post.objects.all()
    context = {
        'title': 'Mainpage',
        'postsList': queryset,
    }
    return render(request, 'posts/postlist.html', context)


def create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request, 'posts/create.html', context)


def detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
        'title': instance.title,
        'instance': instance,
    }
    return render(request, 'posts/detail.html', context)


def update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Updated")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'title': instance.title,
        'instance': instance,
        'form': form,
    }
    return render(request, 'posts/create.html', context)


def delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Удалено")
    return redirect('posts:mainpage')
