from django import forms
from django.contrib.auth import get_user_model
from django.urls import reverse

from .utils import code_generator
from .models import Profile
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    location = forms.CharField(max_length=60)
    bio = forms.TextInput()

    class Meta:
        model = Profile
        fields = ('gender', 'location', 'birth_date', 'bio', 'avatar')


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', )


User = get_user_model()


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = False
        user.save()
        print("Next steps")

        user.profile.activation_key = code_generator()

        path_ = reverse('profiles:activate', kwargs={'code': user.profile.activation_key})
        subject = 'Активация аккаунта papablog.org'
        from_email = settings.DEFAULT_FROM_EMAIL
        message = 'This is my test message'
        recipient = [self.cleaned_data.get("email")]
        html_message = '<p>Привет, {name}!</p><br>' \
                       '<p>Для завершения регистрации пройдите по ссылке: {key}</p>'.format(name=user.username, key=path_)

        send_mail(subject, message, from_email, recipient, fail_silently=False, html_message=html_message)

        if commit:
            user.save()
        return user
