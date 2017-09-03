# Third Party Stuff
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from simple_history.models import HistoricalRecords

# Concierge Stuff
from concierge.base.models import SlugModel, TimeStampedModel, UUIDModel
from concierge.quiz.models import Quiz


class Speaker(UUIDModel, TimeStampedModel):
    history = HistoricalRecords(table_name='event_speaker_history')
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField(unique=True, db_index=True)
    about = models.TextField(blank=True)

    class Meta:
        db_table = 'event_speaker'
        verbose_name = _('Speaker')
        verbose_name_plural = _('Speakers')

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Event(UUIDModel, TimeStampedModel, SlugModel):
    EVENT_CHOICES = (
        ('EVENT', 'EVENT'),
        ('SESSION', 'SESSION'),
        ('MEETUP', 'MEETUP'),
        ('CONFERENCE', 'CONFERENCE'),
        ('TALK', 'TALK'),
        ('WORKSHOP', 'WORKSHOP'),
        ('DEV_SPRINT', 'DEV SPRINT'),
        ('PANEL_DISCUSSION', 'PANEL DISCUSSION'),
        # TODO: BOF & Open Spaces
    )

    VISIBILITY_CHOICES = (
        ('PUBLIC', 'PUBLIC'),
        ('PRIVATE', 'PRIVATE'),
    )

    # Need to be nullable, as the value will be populated after creation of the `Event` instance
    registration_quiz = models.ForeignKey(Quiz, related_name='event_registration', null=True)
    feedback_quiz = models.ForeignKey(Quiz, related_name='event_feedback', null=True)

    history = HistoricalRecords(table_name='event_event_history')
    kind = models.CharField(max_length=15, choices=EVENT_CHOICES)
    happening = models.ForeignKey('self', blank=True, null=True)
    speaker = models.ForeignKey(Speaker, related_name='events', null=True, blank=True)
    venue = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(blank=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    participation_open = models.BooleanField(default=False, help_text='can a user participate in this event')
    participation_start = models.DateTimeField(null=True, blank=True)
    participation_end = models.DateTimeField(null=True, blank=True)
    is_offline = models.BooleanField(default=True)

    class Meta:
        db_table = 'event_event'
        verbose_name = _('Event')
        verbose_name_plural = _('Events')

    def __str__(self):
        return self.slug

    def can_participate(self):
        # Valiation for `participation_start` & `participation_end` is handled by the serializer
        # These value cannot be None
        return bool(self.participation_open and (self.participation_start <= timezone.now() < self.participation_end))


class OfflineEvent(UUIDModel, TimeStampedModel):
    history = HistoricalRecords(table_name='event_offline_event_history')
    event = models.OneToOneField(Event, related_name='offline')
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    address = models.TextField()
    address_guidelines = models.TextField()
    rsvp_open = models.BooleanField(default=False, help_text='can a participant RSVP for this event')
    rsvp_start = models.DateTimeField(null=True, blank=True)
    rsvp_end = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'event_offline_event'
        verbose_name = _('Offline Event')
        verbose_name_plural = _('Offline Events')

    def __str__(self):
        return self.event.slug


class Organisation(UUIDModel, TimeStampedModel, SlugModel):
    ORG_CHOICES = (
        ('HOST', 'HOST'),
        ('SPONSOR', 'SPONSOR'),
        ('OTHER', 'OTHER'),
    )

    history = HistoricalRecords(table_name='organisation_organisation_history')
    kind = models.CharField(max_length=15, choices=ORG_CHOICES)

    class Meta:
        db_table = 'organisation_organisation'
        verbose_name = _('Organisation')
        verbose_name_plural = _('Organisations')

    def __str__(self):
        return self.slug


class SponsorCategory(models.Model):
    """To be added via Admin Panel(or Fixture), prior to adding Sponsors"""
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'event_sponsor_category'
        verbose_name = _('Sponsor Category')
        verbose_name_plural = _('Sponsor Categories')

    def __str__(self):
        return self.name


class Sponsor(TimeStampedModel):
    history = HistoricalRecords(table_name='event_sponsor_history')
    event = models.ForeignKey(Event)
    organisation = models.ForeignKey(Organisation)
    category = models.ForeignKey(SponsorCategory, to_field='name')

    class Meta:
        db_table = 'event_sponsor'
        verbose_name = _('Sponsor')
        verbose_name_plural = _('Sponsors')

    def __str__(self):
        return '{}--{}'.format(self.organisation, self.event)
