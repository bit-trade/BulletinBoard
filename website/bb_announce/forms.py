from django import forms
from .models import Announcement, ReplyAnnounce


class AdvertForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'content', 'announce_cat']


class ReplyForm(forms.ModelForm):
    class Meta:
        model = ReplyAnnounce
        fields = ['text', 'announce']
        # widgets = {
        #     'announce': forms.Select(attrs={'disabled': True})
        # }

