from django.forms import ModelForm

from.models import UserProfilePublicData


class ProfileSettingsForm(ModelForm):
    class Meta:
        model = UserProfilePublicData
        fields = '__all__'
        exclude = ('user', 'profile_followers', 'profile_following')

    def __init__(self, *args, **kwargs):
        super(ProfileSettingsForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False
