from django.urls import reverse
from django.test import TestCase
from django.utils import timezone

from .models import Event, EventSubscription


def create_event(title, description, date, author, state):
    """
    Function to create an Event object
    """
    return Event.objects.create(title=title, description=description,
                                date=date, author=author, state=state)


def create_event_subscription(event, name, email, comment):
    """
    Function to create an EventSubscription object
    """
    return EventSubscription.objects.create(event=event, name=name,
                                            email=email, comment=comment)


class CreateModels(TestCase):

    def test_create_event(self):
        """
        Test to verify the event creation
        """
        event = create_event(title='Title', description='Description',
                             date=timezone.now(), author='Author', state=Event.STATE_UNPUBLISHED)
        event_db = Event.objects.get(pk=event.id)
        self.assertEqual(event, event_db)

    def test_create_event_subscription(self):
        """
        Test to verify the event subscription creation
        """
        event = create_event(title='Title', description='Description',
                             date=timezone.now(), author='Author', state=Event.STATE_UNPUBLISHED)
        event_subscription = create_event_subscription(event=event, name='Name',
                                                       email='email@mailna.me', comment='Comment')
        event_subscription_db = EventSubscription.objects.get(pk=event_subscription.id)
        self.assertEquals(event_subscription, event_subscription_db)


class EventListViewTests(TestCase):

    def test_no_published_events(self):
        """
        Test to verify if there are not published events
        """
        create_event(title='Title', description='Description',
                     date=timezone.now(), author='Author', state=Event.STATE_UNPUBLISHED)

        response = self.client.get(reverse('events:list'))
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['event_list'])

    def test_published_events(self):
        """
        Test to verify if there are published events
        """
        create_event(title='Title', description='Description',
                     date=timezone.now(), author='Author', state=Event.STATE_PUBLISHED)

        response = self.client.get(reverse('events:list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['event_list'])


class EventDetailViewTests(TestCase):

    def test_no_published_event(self):
        """
        Test to verify that the details of an unpublished event cannot be obtained
        """
        event = create_event(title='Title', description='Description',
                     date=timezone.now(), author='Author', state=Event.STATE_UNPUBLISHED)

        response = self.client.get(reverse('events:detail', kwargs={'pk': event.id}))
        self.assertEqual(response.status_code, 404)

    def test_published_event(self):
        """
        Test to verify that the details of a published event can be obtained
        """
        event = create_event(title='Title', description='Description',
                     date=timezone.now(), author='Author', state=Event.STATE_PUBLISHED)

        response = self.client.get(reverse('events:detail', kwargs={'pk': event.id}))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['event'], event)


class EventSubscriptionCreateViewTests(TestCase):

    def test_subscribe_to_no_published_event(self):
        """
        Test to verify that an uses cannot subscribe to an unpublished event
        """
        event = create_event(title='Title', description='Description',
                             date=timezone.now(), author='Author', state=Event.STATE_UNPUBLISHED)

        data = {'name': 'Name', 'email': 'user@mailna.me', 'comment': 'This is a comment'}

        response = self.client.post(reverse('events:subscribe', kwargs={'pk': event.id}), data=data)
        self.assertEqual(response.status_code, 404)

    def test_subscribe_to_published_event(self):
        """
        Test to verify that an uses can subscribe to a published event
        """
        event = create_event(title='Title', description='Description',
                             date=timezone.now(), author='Author', state=Event.STATE_PUBLISHED)

        data = {'name': 'Name', 'email': 'user@mailna.me', 'comment': 'This is a comment'}

        response = self.client.post(reverse('events:subscribe', kwargs={'pk': event.id}), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('events:list'))
        self.assertEqual(EventSubscription.objects.filter(event_id=event.id).count(), 1)
