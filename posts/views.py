from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.http import JsonResponse
from django.http import HttpResponseRedirect

from .forms import AddPostForm
from .models import PostsTable, LikesTable, CommentsTable, RetweetTable


@login_required(redirect_field_name='main_page')
def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user_id = request.user
            obj.primary = True
            obj.save()
            messages.success(request, 'Successfully posted')

    return redirect(reverse_lazy('user_main_page'))


@login_required(redirect_field_name='main_page')
def like_post(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_like')
        post_form = PostsTable.objects.get(pk=post_id)
        # update like count
        if LikesTable.objects.filter(user_id=request.user, post_id=post_form).exists():
            post_form.likes -= 1
            post_form.save()
            like_entry = LikesTable.objects.get(user_id=request.user, post_id=post_form)
            like_entry.delete()
        else:
            post_form.likes += 1
            post_form.save()
            like_form = LikesTable.objects.create(user_id=request.user, post_id=post_form)

            like_form.save()

    return redirect(reverse_lazy('user_main_page'))


@login_required(redirect_field_name='main_page')
def comment_post(request):
    if request.method == 'POST':
        post_form = AddPostForm(request.POST, request.FILES)
        # button submit for getting parent id not optimal as it can be changed by user
        parent_id = request.POST.get('submit', None)
        if parent_id is None:
            raise ValueError

        if post_form.is_valid():
            post_obj = post_form.save(commit=False)
            post_obj.user_id = request.user
            post_obj.primary = False
            post_obj.save()
            post_parent = PostsTable.objects.get(pk=parent_id)
            post_parent.comments += 1
            post_parent.save()
            comment_obj = CommentsTable.objects.create(parent_id=post_parent, child_id=post_obj)
            comment_obj.save()
    return redirect('post_detail', pk=request.POST.get('submit'))

@login_required()
def retweet_post(request):
    if request.method == 'POST':
        post_form = AddPostForm(request.POST, request.FILES)
        # button submit for getting parent id not optimal as it can be changed by user
        parent_id = request.POST.get('submit', None)
        if parent_id is None:
            raise ValueError

        if post_form.is_valid():
            post_obj = post_form.save(commit=False)
            post_obj.user_id = request.user
            post_obj.primary = True
            post_obj.save()
            post_parent = PostsTable.objects.get(pk=parent_id)
            post_parent.shares += 1
            post_parent.save()
            retweet_obj = RetweetTable.objects.create(retweet_parent_id=post_parent,
                                                      retweet_child_id=post_obj)
            retweet_obj.save()
    return redirect('main_page')