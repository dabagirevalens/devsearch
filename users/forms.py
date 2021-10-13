from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,  Skill, Message


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Full Name',
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update(
                {'class': 'input input--text'})


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'username', 'email', 'location',
                  'short_intro', 'bio',  'profile_image',
                  'social_github', 'social_twitter', 'social_linkedin',
                  'social_youtube', 'social_website']

        labels = {
            'name': 'Full Name'
        }

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update(
                {'class': 'input input--text'})


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update(
                {'class': 'input input--text'})


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'message']

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update(
                {'class': 'input input--text'})
