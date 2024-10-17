from django.contrib import admin
from .models import AnnounceCat, Announcement, ReplyAnnounce


class AnnounceCatAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    list_display_links = ('title',)


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'data_creation', 'user', 'announce_cat')
    list_display_links = ('title',)


class ReplyAnnounceAdmin(admin.ModelAdmin):
    list_display = ('id', 'data_creation', 'user', 'announce')
    list_display_links = ('data_creation',)


admin.site.register(AnnounceCat, AnnounceCatAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(ReplyAnnounce, ReplyAnnounceAdmin)
