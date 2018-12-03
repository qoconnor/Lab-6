from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from accounts.forms import EditProfileForm, ImageUploadForm
from accounts.models import UserProfile

# Create your views here.
def home(request):
    numbers = [1,2,3,4,5]
    name = 'Quinn OConnor'

    args = {'name': name, 'numbers': numbers}
    return render(request, 'accounts/home.html', args)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')
    else:
        form = UserCreationForm()

        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)

def view_profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            print("Hello")
            try:
                users = UserProfile.objects.all()
                user = users.get(user=request.user)
                user.song = form.cleaned_data['song']
                user.description = form.cleaned_data['description']
                user.album = form.cleaned_data['album']
                user.artist = form.cleaned_data['artist']
                user.save()
                return redirect('/account/profile')
            except:
                return HttpResponse("Something went wrong")
    else:
        form = EditProfileForm()
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)
    return HttpResponse("Something went wrong")

def upload_pic(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            users = UserProfile.objects.all()
            user = users.get(user=request.user)
            user.image.delete()
            user.image = form.cleaned_data['image']
            user.save()
            return redirect('/account/profile/edit/')
    else:
        form = ImageUploadForm()
    return HttpResponse("Must upload an image")
