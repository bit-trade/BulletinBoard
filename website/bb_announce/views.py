from django.views.generic import ListView, DetailView
from .models import Announcement


class AdvertList(ListView):
    model = Announcement
    ordering = '-data_creation'
    template_name = 'bb_announce/home.html'
    context_object_name = 'adverts'
    paginate_by = 15


class AdvertDetail(DetailView):
    model = Announcement
    context_object_name = 'advert'
    template_name = 'bb_announce/advert.html'
