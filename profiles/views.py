from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView
from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth import get_user_model
from profiles.models import Profile
from .forms import ProfileForm, UserForm, RegisterForm


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


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('posts:mainpage')


def activate_user_view(request, code=None, *args, **kwargs):
    if code:
        qs = Profile.objects.filter(activation_key=code)
        if qs.exists() and qs.count() == 1:
            profile = qs.first()
            if not profile.user.is_active:
                user_ = profile.user
                user_.is_active = True
                user_.save()
                profile.activation_key = False
                profile.save()
                return redirect(reverse_lazy('profiles:login'))
    # invalid code
    return redirect(reverse_lazy('posts:mainpage'))
