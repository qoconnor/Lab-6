from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default='')
    album = models.CharField(max_length=100, default='')
    song = models.CharField(max_length=100, default='')
    artist = models.CharField(max_length=100, default='')
    image = models.ImageField(blank=True, default='default.jpg')

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

class Posts(models.Model):
    fromUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fromUser', null=True)
    title = models.CharField(max_length=50)
    post = models.CharField(max_length=2000)
    album = models.CharField(max_length=100, default='N/A')
    song = models.CharField(max_length=100, default='N/A')
    artist = models.CharField(max_length=100, default='N/A')
    artwork = models.ImageField(blank=True, default='default.jpg')
    public = models.BooleanField(default=False)

class Comments(models.Model):
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commentUser', null=True)
    comment = models.CharField(max_length=300)
    commentPk = models.IntegerField(default='-1')
