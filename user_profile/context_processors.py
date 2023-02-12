from .models import UserFollowTable


def followers(request):
    print(UserFollowTable.objects.filter(follower=request.user.id).select_related('following'))
    return {'followed': UserFollowTable.objects.filter(follower=request.user.id).select_related('following')}
