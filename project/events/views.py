from django.views import generic

from .models import Event


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
