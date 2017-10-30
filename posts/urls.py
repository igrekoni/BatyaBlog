from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import (
        mainpage,
        create,
        detail,
        update,
        delete,
        childs,
        things,
        dosug,
        travel,
        humor,
        TagListView,
    )


urlpatterns = [
    url(r'^$', mainpage, name='mainpage'),
    url(r'^childs/$', childs, name='childs'),
    url(r'^things/$', things, name='things'),
    url(r'^dosug/$', dosug, name='dosug'),
    url(r'^travel/$', travel, name='travel'),
    url(r'^humor/$', humor, name='humor'),
    url(r'^create/$', create),
    url(r'^(?P<slug>[\w-]+)/$', detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', delete),
    url(r'^tag/(?P<slug>[\w-]+)/$', TagListView.as_view(), name='tagged'),



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
