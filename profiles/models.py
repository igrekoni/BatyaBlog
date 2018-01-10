from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# def user_directory_path(instance):
#     # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
#     return 'avatar/{0}'.format(instance.user.username)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/',
                              null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)

    def __unicode__(self):
        return self.user.username

    def __str__(self):
        return self.user.username

    def send_activation_email(self):
        print("Activation")
        pass


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
