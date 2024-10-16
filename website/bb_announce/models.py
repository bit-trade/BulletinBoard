from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User


class AnnounceCat(models.Model):
    title = models.CharField(max_length=40, unique=True)
    description = models.TextField(max_length=500, blank=True)


class Announcement(models.Model):
    title = models.CharField(max_length=250)
    content = HTMLField()
    data_creation = models.DateTimeField(auto_now_add=True)
    data_last_updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='announce_user_feedback')


class ReplyAnnounce(models.Model):
    text = models.TextField(max_length=500)
    data_creation = models.DateTimeField(auto_now_add=True)
    data_last_updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reply_user_feedback')
    announce = models.ForeignKey(Announcement, on_delete=models.RESTRICT, related_name='reply_announce_feedback')

    def __str__(self):
        return f'откликнулись - {self.data_creation}'
