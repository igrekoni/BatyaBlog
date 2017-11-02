from django.http import Http404, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Post
from .forms import PostForm
from django.views.generic import ListView, DetailView, CreateView


class Mainpage(ListView):
    template_name = "posts/postlist.html"
    paginate_by = "3"

    def get_queryset(self):
        return Post.objects.all()


# class Create(CreateView):
#     template_name = 'posts/create.html'
#     model = Post
#     fields = [
#         'title',
#         'image',
#         'previewText',
#         'fullText',
#         'category',
#         'tags',
#         'draft',
#         'publish',
#     ]


def create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, "Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request, 'posts/create.html', context)


class Detail(DetailView):
    template_name = 'posts/detail.html'
    model = Post


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
#              PAGES CLASSES
#


class Childs(ListView):
    template_name = "posts/postlist.html"
    paginate_by = "3"

    def get_queryset(self):
        return Post.objects.all().filter(category__iexact='Дети')


class Things(ListView):
    template_name = "posts/postlist.html"
    paginate_by = "3"

    def get_queryset(self):
        return Post.objects.all().filter(category__iexact='Вещи')


class Dosug(ListView):
    template_name = "posts/postlist.html"
    paginate_by = "3"

    def get_queryset(self):
        return Post.objects.all().filter(category__iexact='Досуг')


class Travel(ListView):
    template_name = "posts/postlist.html"
    paginate_by = "3"

    def get_queryset(self):
        return Post.objects.all().filter(category__iexact='Путешествия')


class Humor(ListView):
    template_name = "posts/postlist.html"
    paginate_by = "3"

    def get_queryset(self):
        return Post.objects.all().filter(category__iexact='Юмор')


class TagListView(ListView):
    template_name = "posts/postlist.html"
    paginate_by = "3"

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs.get("slug")).all()

    def get_context_data(self, **kwargs):
        context = super(TagListView, self).get_context_data(**kwargs)
        context["tag"] = self.kwargs.get("slug")
        return context


# class CategoryListView(ListView):
#     template_name = "posts/postlist.html"
#     paginate_by = "3"
#
#     def get_queryset(self):
#         return Post.objects.filter(category=self).all()
#
#     def get_context_data(self, **kwargs):
#         context = super(CategoryListView, self).get_context_data(**kwargs)
#         context["category"] = self.kwargs.get("category")
#         return context
