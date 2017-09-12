from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'image',
            'previewText',
            'fullText',
            'category',
            'draft',
            'publish',
        ]