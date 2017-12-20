from django.contrib import admin
from .models import Profile


class ProfileModelAdmin(admin.ModelAdmin):

    class Meta:
        model = Profile


admin.site.register(Profile, ProfileModelAdmin)
