from django import forms
from django.contrib.auth.models import User
from accounts.models import UserProfile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class EditProfileForm(UserChangeForm):

    class Meta:
        model = UserProfile
        fields = (
            'description',
            'song',
            'album',
            'artist',
            'password',
        )
