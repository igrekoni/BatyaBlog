from django.contrib import admin
from .models import Post


class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp', 'category']
    list_display_links = ['title', 'category']
    list_filter = ['timestamp', 'updated']
    search_fields = ['title']

    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)

