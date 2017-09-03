from django.conf.urls import url
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
    url(r'^(?P<id>\d+)/$', detail, name='detail'),
    url(r'^(?P<id>\d+)/edit/$', update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', delete),
]
