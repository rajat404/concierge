from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from simple_history.models import HistoricalRecords

from concierge.base.models import (TimeStampedModel, TimeStampedSlugModel,
                                   TimeStampedUUIDModel, UUIDModel)
from concierge.quiz.models import Quiz


class Speaker(TimeStampedUUIDModel):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField(unique=True, db_index=True)
    about = models.TextField(blank=True)
    history = HistoricalRecords(table_name='concourse_speaker_history')

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        db_table = 'concourse_speaker'
        verbose_name = _('Speaker')
        verbose_name_plural = _('Speakers')


class Concourse(TimeStampedSlugModel, UUIDModel):
    CONCOURSE_CHOICES = (
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

    STATE_CHOICES = (
        ('PUBLIC', 'PUBLIC'),
        ('PRIVATE', 'PRIVATE'),
    )

    kind = models.CharField(max_length=15, choices=CONCOURSE_CHOICES)
    event = models.ForeignKey("self", blank=True, null=True, to_field='slug')
    speaker = models.ForeignKey(Speaker, related_name='concourses', null=True, blank=True)
    venue = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(blank=True)
    # Need to be nullable temporarily, as the value will be populated in the post_save method
    registration_quiz = models.ForeignKey(Quiz, related_name='concourse_registration', null=True, blank=True)
    feedback_quiz = models.ForeignKey(Quiz, related_name='concourse_feedback', null=True, blank=True)
    # Issue in migration due to self-referencing foreign key
    # history = HistoricalRecords(table_name='concourse_concourse_history')
    start = models.DateTimeField()
    end = models.DateTimeField(null=True, blank=True)
    participation_open = models.BooleanField(default=False, help_text='can a user participate in this concourse')
    is_offline = models.BooleanField(default=True)

    class Meta:
        db_table = 'concourse_concourse'
        verbose_name = _('Concourse')
        verbose_name_plural = _('Concourses')

    def __str__(self):
        return self.slug


def _create_quiz(slug, model_name):
    """Returns a Quiz object with the label
    of the specified FK and Concourse's Slug
    """
    label = '{}-{}'.format(slug, model_name)
    quiz_obj, _ = Quiz.objects.get_or_create(label=label)
    return quiz_obj


@receiver(post_save, sender=Concourse)
def populate_concourse_fk(sender, instance=None, created=False, **kwargs):
    """Sets foreign key relation to Quiz objects, with the appropriate label,
    for the newly created Concourse objects

    Also creates the associated OfflineConcourse object, if the said
    concourse is offline
    """
    if created:
        _slug = instance.slug
        instance.registration_quiz = _create_quiz(_slug, 'registration')
        instance.feedback_quiz = _create_quiz(_slug, 'feedback')
        instance.save()

        if instance.is_offline:
            OfflineConcourse.objects.get_or_create(concourse=instance)


class OfflineConcourse(TimeStampedUUIDModel):
    concourse = models.OneToOneField(Concourse, related_name='offline')
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    address = models.TextField()
    address_guidelines = models.TextField()
    history = HistoricalRecords(table_name='concourse_offline_concourse_history')

    class Meta:
        db_table = 'concourse_offline_concourse'
        verbose_name = _('Offline Concourse')
        verbose_name_plural = _('Offline Concourses')

    def __str__(self):
        return self.concourse.slug


class Organisation(TimeStampedSlugModel):
    ORG_CHOICES = (
        ('HOST', 'HOST'),
        ('SPONSOR', 'SPONSOR'),
        ('OTHER', 'OTHER'),
    )

    kind = models.CharField(max_length=15, choices=ORG_CHOICES)
    history = HistoricalRecords(table_name='organisation_organisation_history')

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
        db_table = 'concourse_sponsor_category'
        verbose_name = _('Sponsor Category')
        verbose_name_plural = _('Sponsor Categories')

    def __str__(self):
        return self.name


class Sponsor(TimeStampedModel):
    concourse = models.ForeignKey(Concourse, to_field='slug')
    organisation = models.ForeignKey(Organisation, to_field='slug', null=True, blank=True)
    category = models.ForeignKey(SponsorCategory, to_field='name')
    history = HistoricalRecords(table_name='concourse_sponsor_history')

    class Meta:
        db_table = 'concourse_sponsor'
        verbose_name = _('Sponsor')
        verbose_name_plural = _('Sponsors')
