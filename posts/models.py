from django.db import models
from django.contrib.auth import models as auth_models
from django.utils.timezone import now


class PostsTable(models.Model):
    user_id = models.ForeignKey(auth_models.User, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    likes = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    post_date = models.DateTimeField(default=now)
    primary = models.BooleanField(default=False)


class LikesTable(models.Model):
    user_id = models.ForeignKey(auth_models.User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(PostsTable, on_delete=models.CASCADE)


class CommentsTable(models.Model):
    parent_id = models.ForeignKey(PostsTable, on_delete=models.CASCADE, related_name="parent_id")
    child_id = models.ForeignKey(PostsTable, on_delete=models.CASCADE, related_name="child_id")


class RetweetTable(models.Model):
    parent_id = models.ForeignKey(PostsTable, on_delete=models.CASCADE, related_name='retweet_parent_id')
    post_id = models.ForeignKey(PostsTable, on_delete=models.CASCADE, related_name='retweet_child_id')
