from django.conf.urls import url
from .views import ProfileDetailView, profile_update
from django.contrib.auth.views import login, logout
from .views import RegisterView, activate_user_view


urlpatterns = [
    url(r'^register/$', RegisterView.as_view(), name='signup'),
    url(r'^activate/(?P<code>[a-z0-9].*)/$', activate_user_view, name='activate'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
    url(r'^(?P<username>[\w-]+)/$', ProfileDetailView.as_view(), name='user'),
    url(r'^(?P<username>[\w-]+)/update/$', profile_update, name='update'),
]
