from django.forms.models import ModelForm

from .models import PostsTable


class AddPostForm(ModelForm):
    class Meta:
        model = PostsTable
        fields = ['content']
