from django.http import Http404, HttpResponseRedirect, request
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.db.models import Q
from .models import Post
from .forms import PostForm
from django.views.generic import ListView, DetailView
from taggit.models import Tag


class Mainpage(ListView):
    template_name = "posts/postlist.html"
    paginate_by = "3"
    all_tags = Tag.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_tags'] = Tag.objects.all()
        return context

    def get_queryset(self):
        q = self.request
        q = str(q)

        query = self.request.GET.get('q')
        print(query)
        if query:
            return Post.objects.all().filter(
                Q(title__icontains=query) |
                Q(category__icontains=query) |
                Q(previewText__icontains=query) |
                Q(fullText__icontains=query) |
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query)
            )

        if self.request.method == 'GET' and '/health/' in q:
            return Post.objects.all().filter(category__iexact='Здоровье')
        elif self.request.method == 'GET' and '/things/' in q:
            return Post.objects.all().filter(category__iexact='Вещи')
        elif self.request.method == 'GET' and '/growth/' in q:
            return Post.objects.all().filter(category__iexact='Развитие')
        elif self.request.method == 'GET' and '/dosug/' in q:
            return Post.objects.all().filter(category__iexact='Досуг')
        else:
            return Post.objects.all()


def create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
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


class Detail(DetailView):
    template_name = 'posts/detail.html'
    model = Post


def update(request, slug=None, *args, **kwargs):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
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


class TagListView(ListView):
    template_name = "posts/postlist.html"
    paginate_by = "3"

    def get_queryset(self, *args, **kwargs):
        return Post.objects.filter(tags__slug=self.kwargs.get("slug")).all()

    def get_context_data(self, *args, **kwargs):
        context = super(TagListView, self).get_context_data(**kwargs)
        context["tag"] = self.kwargs.get("slug")
        return context


def robots(request):
    return render_to_response('robots.txt', content_type='text/plain')

#
#              PAGES CLASSES
#


# class Health(ListView):
#     template_name = "posts/postlist.html"
#     paginate_by = "3"
#
#     def get_queryset(self):
#         q = self.request
#         q = str(q)
#         print(q)
#
#         if self.request.method == 'GET' and '/health/' in q:
#             return Post.objects.all().filter(category__iexact='Здоровье')
#         elif self.request.method == 'GET' and '/things/' in q:
#             return Post.objects.all().filter(category__iexact='Досуг')
#         elif self.request.method == 'GET' and '/things/' in q:
#             return Post.objects.all().filter(category__iexact='Досуг')
#         elif self.request.method == 'GET' and '/things/' in q:
#             return Post.objects.all().filter(category__iexact='Досуг')
#         else:
#             return Post.objects.all()
#
#
# class Things(ListView):
#     template_name = "posts/postlist.html"
#     paginate_by = "3"
#
#     def get_queryset(self):
#         return Post.objects.all().filter(category__iexact='Вещи')
#
#
# class Dosug(ListView):
#     template_name = "posts/postlist.html"
#     paginate_by = "3"
#
#     def get_queryset(self):
#         return Post.objects.all().filter(category__iexact='Досуг')
#
#
# class Growth(ListView):
#     template_name = "posts/postlist.html"
#     paginate_by = "3"
#
#     def get_queryset(self):
#         return Post.objects.all().filter(category__iexact='Развитие')
