from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import (
        mainpage,
        create,
        detail,
        update,
        delete,
    )


urlpatterns = [
    url(r'^$', mainpage, name='mainpage'),
    url(r'^create/$', create),
    url(r'^(?P<slug>[\w-]+)/$', detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', delete),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
