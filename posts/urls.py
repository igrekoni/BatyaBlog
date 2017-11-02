from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import (
        Mainpage,
        create,
        Detail,
        update,
        delete,
        Childs,
        Things,
        Dosug,
        Travel,
        Humor,
        TagListView,
        # CategoryListView,
    )


urlpatterns = [
    url(r'^$', Mainpage.as_view(), name='mainpage'),
    url(r'^childs/$', Childs.as_view(), name='childs'),
    url(r'^things/$', Things.as_view(), name='things'),
    url(r'^dosug/$', Dosug.as_view(), name='dosug'),
    url(r'^travel/$', Travel.as_view(), name='travel'),
    url(r'^humor/$', Humor.as_view(), name='humor'),
    url(r'^create/$', create, name='create'),
    url(r'^(?P<slug>[\w-]+)/$', Detail.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', delete),
    url(r'^tag/(?P<slug>[\w-]+)/$', TagListView.as_view(), name='tagged'),
    # url(r'^category/(?P<slug>[\w-]+)/$', CategoryListView.as_view(), name='categorized'),



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
