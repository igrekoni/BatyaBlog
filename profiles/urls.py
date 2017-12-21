from django.conf.urls import url
from .views import ProfileDetailView, profile_update


urlpatterns = [
    url(r'^(?P<username>[\w-]+)/$', ProfileDetailView.as_view(), name='user'),
    url(r'^(?P<username>[\w-]+)/update/$', profile_update, name='update'),
]
