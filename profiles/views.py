from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.contrib.auth import get_user_model


User = get_user_model()


class ProfileDetailView(DetailView):
    template_name = 'user.html'

    def get_object(self, queryset=None):
        username = self.kwargs.get('username', None)
        if username is None:
            raise Http404
        return get_object_or_404(User, username__iexact=username, is_active=True)
