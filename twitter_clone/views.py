from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, ListView

from posts.models import PostsTable, LikesTable, CommentsTable


def popular_posts():
    posts = PostsTable.objects.filter(primary=True).select_related('user_id').order_by('-post_date')
    context_feed = [{'content': i, 'content_user': i.user_id} for i in posts]
    return context_feed


class MainPageView(TemplateView):
    template_name = "components/pages/index.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('user_main_page'))
        else:
            context_feed = popular_posts()
            return render(request, self.template_name, {'content_list': context_feed})


class SettingsPageView(TemplateView):
    template_name = "components/pages/settings.html"


class UserMainPage(TemplateView):
    template_name = "components/pages/home.html"

    def get_context_data(self, **kwargs):
        posts = popular_posts()
        liked = LikesTable.objects.filter(user_id=self.request.user)
        liked = [i['post_id_id'] for i in liked.values()]
        return {'content_list': posts, 'liked': liked}


class UserPostDetailView(DetailView):
    model = PostsTable
    template_name = "components/pages/content-detail.html"

    def get_context_data(self, **kwargs):
        context = super(UserPostDetailView, self).get_context_data(**kwargs)
        comments = CommentsTable.objects.filter(parent_id=self.object.pk)
        comments = [i.child_id for i in comments]
        if self.request.user.is_authenticated:
            liked = LikesTable.objects.filter(user_id=self.request.user)
            liked = [i['post_id_id'] for i in liked.values()]
        else:
            liked = None
        context['commentstable_set'] = sorted(comments, key=lambda x: x.post_date, reverse=True)
        context['liked'] = liked
        return context


class UserSearchView(TemplateView):
    template_name = "components/pages/user/search.html"


class TestView(TemplateView):
    template_name = "components/pages/index.html"
