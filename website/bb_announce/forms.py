from django import forms
from .models import Announcement


class AdvertForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'content', 'announce_cat', 'user' ]

