from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.flatpages import urls
from django.contrib.sitemaps.views import sitemap
from posts.sitemap import ASitemap


sitemaps = {
    'posts': ASitemap()
}


urlpatterns = [
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    url(r'^user/', include("profiles.urls", namespace='profiles')),
    url(r'^admin/', admin.site.urls),
    url(r'^pages/', include(urls)),
    url(r'^', include("posts.urls", namespace='posts')),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
