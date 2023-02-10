from django.urls import path
from .views import add_post, like_post, comment_post
from django.contrib.auth.decorators import login_required

app_name = 'posts'
urlpatterns = [
    path('add_post/', add_post, name='add_post'),
    path('like_post/', like_post, name='like_post'),
    path('comment_post/', comment_post, name='comment_post'),
]
