from django.conf.urls import include, url
from django.contrib import admin
from posts import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include("posts.urls", namespace='posts')),
]
