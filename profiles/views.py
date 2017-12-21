from django.contrib import messages
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.contrib.auth import get_user_model
from .forms import ProfileForm, UserForm


User = get_user_model()


class ProfileDetailView(DetailView):
    template_name = 'user.html'

    def get_object(self, queryset=None):
        username = self.kwargs.get('username', None)
        if username is None:
            raise Http404
        return get_object_or_404(User, username__iexact=username, is_active=True)


def profile_update(request, *args, **kwargs):
    user_form = UserForm(request.POST, instance=request.user)
    profile_form = ProfileForm(request.POST, instance=request.user.profile)
    if request.method == 'POST':

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Ваш профиль был успешно обновлен!')
            return render(request, 'user.html', {})
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'update.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
