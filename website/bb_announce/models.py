from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField
from django.contrib.auth.models import User


class AnnounceCat(models.Model):
    class CategoryName(models.TextChoices):
        TANKS = 'TK', 'Танки'
        HILLS = 'HL', 'Хилы'
        DD = 'DD', 'ДД'
        MERCHANTS = 'ME', 'Торговцы'
        GUILDMASTERS = 'GM', 'Гилдмастеры'
        QUESTGIVERS = 'QG', 'Квестгиверы'
        BLACKSMITHS = 'BM', 'Кузнецы'
        TANNERS = 'TN', 'Кожевники'
        POTIONISTS = 'PO', 'Зельевары'
        SPELLCASTERS = 'SC', 'Мастера заклинаний'

    title = models.CharField(max_length=20, unique=True, choices=CategoryName, default=CategoryName.TANKS)
    description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.title


class Announcement(models.Model):
    title = models.CharField(max_length=170)
    content = HTMLField()
    data_creation = models.DateTimeField(auto_now_add=True)
    data_last_updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Announce_User_feedback')
    announce_cat = models.ForeignKey(AnnounceCat, on_delete=models.CASCADE, null=True,
                                     related_name='Announce_AnnounceCat_feedback')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return f'/news/{self.id}'
        return reverse('advert_detail', args=[str(self.id)])


class ReplyAnnounce(models.Model):
    text = models.TextField(max_length=1000)
    data_creation = models.DateTimeField(auto_now_add=True)
    data_last_updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Reply_User_feedback')
    announce = models.ForeignKey(Announcement, on_delete=models.RESTRICT, related_name='Reply_Announce_feedback')

    def __str__(self):
        return f'откликнулись - {self.data_creation}'

