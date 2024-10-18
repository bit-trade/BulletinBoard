from django.views.generic import ListView
from .models import Announcement


class AnnouncementList(ListView):
    model = Announcement
    ordering = '-data_creation'
    template_name = 'bb_announce/home.html'
    context_object_name = 'announcements'
    paginate_by = 15



