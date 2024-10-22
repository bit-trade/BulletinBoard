from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Announcement
from .forms import AdvertForm


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


class AdvertCreate(CreateView):
    form_class = AdvertForm
    model = Announcement
    template_name = 'bb_announce/advert_create.html'

    def form_invalid(self, form):
        advert = form.save(commit=False)
        advert.user = self.request.user
        return super().form_valid(form)


class AdvertUpdate(UpdateView):
    form_class = AdvertForm
    model = Announcement
    template_name = 'bb_announce/advert_edit.html'


class AdvertDelete(DeleteView):
    model = Announcement
    template_name = 'bb_announce/advert_delete.html'
    success_url = reverse_lazy('home')

