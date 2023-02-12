from django.urls import path

from .views import UserProfileSettings, follow_user

app_name = "user_profile"
urlpatterns = [
    path("settings/", UserProfileSettings.as_view(), name="settings"),
    path("follow/", follow_user, name='follow'),
]
