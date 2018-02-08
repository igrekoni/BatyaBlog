from django.db import models
from django.utils.text import slugify
from unidecode import unidecode
from posts.utils import categories
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from taggit.managers import TaggableManager


def upload_location(instance, filename):
    return "%s/%s" % (instance.id, filename)


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=150, blank=False)
    image = models.ImageField(upload_to=upload_location,
                              null=True, blank=True, height_field='height_field', width_field='width_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    previewText = models.TextField(max_length=260, blank=True)
    fullText = models.TextField()
    slug = models.SlugField(max_length=150, unique=True)
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    category = models.CharField(max_length=40, choices=categories(), default='CH')
    tags = TaggableManager(blank=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self, *args, **kwargs):
        if self.category == u'Здоровье':
            cat = "health"
        elif self.category == u'Развитие':
            cat = "growth"
        elif self.category == u'Вещи':
            cat = "things"
        elif self.category == u'Досуг':
            cat = "dosug"
        return reverse("posts:detail", kwargs={"category": cat, "slug": self.slug})

    class Meta:
        ordering = ["-timestamp"]


def create_slug(instance, new_slug=None):
    slug = slugify(unidecode(instance.title))
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (instance, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Post)
