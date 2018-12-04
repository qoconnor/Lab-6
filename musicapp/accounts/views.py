from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from accounts.forms import EditProfileForm, ImageUploadForm, CreatePostForm
from accounts.models import UserProfile, Posts

# Create your views here.
def home(request):
    posts = Posts.objects.all().order_by("-id")
    args = {'posts': posts}
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

def create_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            #try:
                obj = Posts.objects.create()
                obj.fromUser = request.user
                obj.post = form.cleaned_data['post']
                obj.title = form.cleaned_data['title']
                obj.album = form.cleaned_data['album']
                obj.song = form.cleaned_data['song']
                obj.artist = form.cleaned_data['artist']
                obj.public = form.cleaned_data['public']
                obj.save()
                return render(request, 'accounts/home.html') #Need to edit later
            #except:
                #return HttpResponse('Something went wrong when creating a post.')
    else:
        form = CreatePostForm()
        args = {'form': form}
        return render(request, 'accounts/create_post.html', args)
    return HttpResponse('Something went wrong')

def view_post(request, pk):
    post = Posts.objects.get(pk=pk)
    args = {'post': post}
    return render(request, 'accounts/view_post.html', args)
