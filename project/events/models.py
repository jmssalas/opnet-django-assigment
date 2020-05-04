from django.db import models


class Event(models.Model):
    STATE_PUBLISHED = 1
    STATE_UNPUBLISHED = 2
    STATES = (
        (STATE_PUBLISHED, 'Published'),
        (STATE_UNPUBLISHED, 'Unpublished')
    )

    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date = models.DateTimeField()
    author = models.CharField(max_length=200)
    state = models.IntegerField(choices=STATES)

    def __str__(self):
        return self.title


class EventSubscription(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    comment = models.CharField(max_length=1000)

    def __str__(self):
        return self.email + "_" + self.event
