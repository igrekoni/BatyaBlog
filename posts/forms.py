from django import forms
from .models import Post
from pagedown.widgets import PagedownWidget


class PostForm(forms.ModelForm):
    previewText = forms.CharField(widget=PagedownWidget)
    fullText = forms.CharField(widget=PagedownWidget)
    publish = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Post
        fields = [
            'title',
            'draft',
            'image',
            'previewText',
            'fullText',
            'category',
            'publish',
        ]
