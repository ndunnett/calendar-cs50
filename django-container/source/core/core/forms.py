from django.forms import ModelForm

from cal.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['mobile']