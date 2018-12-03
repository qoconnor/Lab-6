from django import forms
from django.contrib.auth.models import User
from accounts.models import UserProfile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class EditProfileForm(forms.Form):
    description = forms.CharField(label='Bio:')
    song = forms.CharField(label='Favorite Song:')
    artist = forms.CharField(label='Favorite Artist:')
    album = forms.CharField(label='Favorite Album:')

class ImageUploadForm(forms.Form):
    image = forms.ImageField()

class CreatePostForm(forms.Form):
    artwork = forms.ImageField()
    title = forms.CharField()
    post = forms.CharField(label='Post:', required=True)
    album = forms.CharField(label='Album:', required=False)
    song = forms.CharField(label='Song:', required=False)
    artist = forms.CharField(label='Artist:', required=False)
    public = forms.BooleanField()
