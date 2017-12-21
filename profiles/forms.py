from django import forms
from .models import Profile
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
