from django import forms
from django.contrib.auth.models import User
from accounts.models import UserProfile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class EditProfileForm(forms.Form):
    description = forms.CharField(label='Bio:', required=False)
    song = forms.CharField(label='Favorite Song:', required=False)
    artist = forms.CharField(label='Favorite Artist:', required=False)
    album = forms.CharField(label='Favorite Album:', required=False)

class ImageUploadForm(forms.Form):
    image = forms.ImageField()

class CreatePostForm(forms.Form):
    title = forms.CharField(label='Title:', required=True)
    post = forms.CharField(label='Description:', required=True)
    album = forms.CharField(label='Album:', required=False)
    song = forms.CharField(label='Song:', required=False)
    artist = forms.CharField(label='Artist:', required=False)

class CreateCommentForm(forms.Form):
    comment = forms.CharField(label='Comment:', required=True)
