from django.urls import reverse_lazy
from django.views import generic

from .models import Event, EventSubscription


class EventListView(generic.ListView):
    model = Event

    def get_queryset(self):
        """Return the published events."""
        return Event.objects.filter(state=Event.STATE_PUBLISHED)


class EventDetailView(generic.DetailView):
    model = Event

    def get_queryset(self):
        """Return the published events."""
        return Event.objects.filter(state=Event.STATE_PUBLISHED)


class EventSubscriptionCreateView(generic.edit.CreateView):
    model = EventSubscription
    fields = ['name', 'email', 'comment']
    success_url = reverse_lazy('events:list')

    def form_valid(self, form):
        form.instance.event_id = self.kwargs['pk']
        return super().form_valid(form)
