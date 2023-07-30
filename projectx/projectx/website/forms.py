from django import forms
from .models import UserProfile, CustomUser
#from .models import Poem
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.forms import BaseUserCreationForm
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from . import models


User = get_user_model()

class UserCreationForm1(UserCreationForm):

    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email","username")


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'gender', 'birthday']


class UserCommentForm(forms.ModelForm):
    class Meta:
        model = models.CommentSection
        fields = ['comment', 'verse_title']



