from django.db import models
from django.contrib.auth.models import User
import uuid
import os
from datetime import date


class UploadTo:

    def _base_func(self, instance, filename, directory):
        def get_path(instance, filename):
            ext = filename.split('.')[-1]
            filename = "%s.%s" % (uuid.uuid4(), ext)
            print(os.path.join(directory, filename))
            return os.path.join(directory, filename)

        print(get_path)
        return get_path

    def profile_image(self, instance, filename):
        print('profile')
        return self._base_func(instance, filename, 'media/profile/image/%Y/%M/%D/')

    def profile_banner(self, instance, filename):
        return self._base_func(instance, filename, 'media/profile/banner/%Y/%M/%D/')


def get_path(instance, filename, directory):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    print(os.path.join(directory, filename))
    return os.path.join(directory, filename)


def get_path_image(instance, filename):
    today = date.today()
    today_path = today.strftime("%Y/%m/%d")
    directory = f'media/profile/image/{today_path}/'
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    print(os.path.join(directory, filename))
    return os.path.join(directory, filename)


def get_path_banner(instance, filename):
    today = date.today()
    today_path = today.strftime("%Y/%m/%d")
    directory = f'media/profile/banner/{today_path}/'
    print(directory)
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    print(os.path.join(directory, filename))
    return os.path.join(directory, filename)


class UserFollowTable(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower_id')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following_id')


class UserProfilePublicData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(null=True, upload_to=get_path_image)
    profile_banner = models.ImageField(null=True, upload_to=get_path_banner)
    profile_bio = models.TextField(null=True)
    profile_url = models.URLField(null=True, max_length=200)
    profile_followers = models.IntegerField(default=0)
    profile_following = models.IntegerField(default=0)
