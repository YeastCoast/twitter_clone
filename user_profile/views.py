from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import UpdateView, TemplateView
from django.forms import forms
from django.http import HttpResponse

from .models import UserFollowTable
from .forms import ProfileSettingsForm


@login_required
def follow_user(request):
    if request.method == 'POST':
        user_id = request.POST.get('follow')
        following = User.objects.get(pk=user_id)
        follower = request.user
        follower_check = UserFollowTable.objects.filter(follower=follower, following=following)
        if follower_check.exists():
            follower_check.delete()
        else:
            follower_obj = UserFollowTable.objects.create(follower=follower, following=following)
            follower_obj.save()

    return HttpResponse()


class UserProfileSettings(TemplateView):
    template_name = "components/pages/profile-settings.html"

    def post(self, request, **kwargs):
        form = ProfileSettingsForm(self.request.POST,
                                   self.request.FILES,
                                   instance=request.user.userprofilepublicdata)
        if form.is_valid():
            print(form.data)
            print('form is valid')
            form.save()

        return redirect(reverse('user_profile:settings'))

    def get(self, request, *args, **kwargs):
        form = ProfileSettingsForm(instance=request.user.userprofilepublicdata)
        context = {'profile_settings': form}
        return render(request, self.template_name, context)

