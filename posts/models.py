from django.db import models
from posts.utils import categories
from django.conf import settings
from django.core.urlresolvers import reverse


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    title = models.CharField(max_length=120, blank=False)
    image = models.FileField(null=True, blank=True)
    previewText = models.TextField(max_length=260, blank=True)
    fullText = models.TextField()
    #publish = models.DateField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    category = models.CharField(max_length=40, choices=categories(), default='CH')

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"id": self.id})

    class Meta:
        ordering = ["-timestamp"]
