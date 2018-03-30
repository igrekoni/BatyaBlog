from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import (
        Mainpage,
        create,
        Detail,
        update,
        delete,
        TagListView,
        robots,
    )


urlpatterns = [
    url(r'^$', Mainpage.as_view(), name='mainpage'),
    url(r'^health/$', Mainpage.as_view(), name='health'),
    url(r'^growth/$', Mainpage.as_view(), name='growth'),
    url(r'^things/$', Mainpage.as_view(), name='things'),
    url(r'^dosug/$', Mainpage.as_view(), name='dosug'),
    url(r'^create/$', create, name='create'),
    url(r'^tag/(?P<slug>[\w-]+)/$', TagListView.as_view(), name='tagged'),
    url(r'^(?P<category>[\w-]+)/(?P<slug>[\w-]+)/$', Detail.as_view(), name='detail'),
    url(r'^(?P<category>[\w-]+)/(?P<slug>[\w-]+)/edit/$', update, name='update'),
    url(r'^(?P<category>[\w-]+)/(?P<slug>[\w-]+)/delete/$', delete),

    url(r'^robots.txt$', robots),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
