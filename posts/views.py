from django.http import Http404, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import Post
from .forms import PostForm
from django.views.generic import ListView


def mainpage(request):
    queryset_list = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(fullText__icontains=query) |
            Q(previewText__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)
            ).distinct()
    paginator = Paginator(queryset_list, 5)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        'postsList': queryset,
        'page_request_var': page_request_var
    }
    return render(request, 'posts/postlist.html', context)


def create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    form = PostForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            form.save_m2m()
            messages.success(request, "Created")
            return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request, 'posts/create.html', context)


def detail(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    context = {
        'instance': instance,
    }
    return render(request, 'posts/detail.html', context)


def update(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Updated")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'instance': instance,
        'form': form,
    }
    return render(request, 'posts/create.html', context)


def delete(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request, "Удалено")
    return redirect('posts:mainpage')


#
#              PAGES FUNCTIONS
#


def childs(request):
    queryset_list = Post.objects.all().filter(category__iexact='Дети')
    paginator = Paginator(queryset_list, 5)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        'postsList': queryset,
        'page_request_var': page_request_var
    }
    return render(request, 'pages/childs.html', context)


def things(request):
    queryset_list = Post.objects.all().filter(category__iexact='Вещи')
    paginator = Paginator(queryset_list, 5)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        'postsList': queryset,
        'page_request_var': page_request_var
    }
    return render(request, 'pages/things.html', context)


def dosug(request):
    queryset_list = Post.objects.all().filter(category__iexact='Досуг')
    paginator = Paginator(queryset_list, 5)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        'postsList': queryset,
        'page_request_var': page_request_var
    }
    return render(request, 'pages/dosug.html', context)


def travel(request):
    queryset_list = Post.objects.all().filter(category__iexact='Путешествия')
    paginator = Paginator(queryset_list, 5)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        'postsList': queryset,
        'page_request_var': page_request_var
    }
    return render(request, 'pages/travel.html', context)


def humor(request):
    queryset_list = Post.objects.all().filter(category__iexact='Юмор')
    paginator = Paginator(queryset_list, 5)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        'postsList': queryset,
        'page_request_var': page_request_var
    }
    return render(request, 'pages/humor.html', context)


class TagListView(ListView):
    template_name = "index.html"

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs.get("slug")).all()

    def get_context_data(self, **kwargs):
        context = super(TagListView, self).get_context_data(**kwargs)
        context["tag"] = self.kwargs.get("slug")
        return context
