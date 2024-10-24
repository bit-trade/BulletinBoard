from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Announcement, ReplyAnnounce
from .forms import AdvertForm, ReplyForm


class AdvertList(ListView):
    model = Announcement
    ordering = '-data_creation'
    html = 'bb_announce/home.html'
    template_name = html
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

    def form_valid(self, form):
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


class ReplyCreate(CreateView):
    model = ReplyAnnounce
    template_name = 'bb_announce/reply_create.html'
    form_class = ReplyForm

    def get_initial(self, *args, **kwargs):
        initial = super(ReplyCreate, self).get_initial(**kwargs)
        initial['announce'] = Announcement.objects.get(pk=self.kwargs['pk'])
        return initial

    def form_valid(self, form):
        reply = form.save(commit=False)
        reply.user = self.request.user
        return super().form_valid(form)


class ReplyUpdate(UpdateView):
    model = ReplyAnnounce
    template_name = 'bb_announce/reply_edit.html'
    form_class = ReplyForm


class ReplyDelete(DeleteView):
    model = ReplyAnnounce
    template_name = 'bb_announce/reply_delete.html'
    success_url = reverse_lazy('home')

