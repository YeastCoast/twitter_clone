"""twitter_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import MainPageView, SettingsPageView, UserMainPage, UserPostDetailView, UserSearchView, TestView, UserProfileView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPageView.as_view(), name='main_page'),
    path('settings/', SettingsPageView.as_view(), name='settings_page'),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path('home/', login_required(UserMainPage.as_view(), login_url='main_page'), name='user_main_page'),
    path('posts/', include('posts.urls')),
    path('post/<int:pk>/', UserPostDetailView.as_view(), name='post_detail'),
    path("__reload__/", include("django_browser_reload.urls")),
    path('home/search', login_required(UserSearchView.as_view(), login_url='main_page'), name='user_search'),
    path('test/', TestView.as_view(), name='testing'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='user_profile'),
]
