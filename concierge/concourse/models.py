from django.db import models
from django.utils.translation import ugettext_lazy as _
from concierge.base.models import TimeStampedModel, TimeStampedSlugModel


class Organisation(TimeStampedSlugModel):
    ORG_TYPE = (
        ('HOST', 'HOST'),
        ('SPONSOR', 'SPONSOR'),
        ('OTHER', 'OTHER'),
    )

    kind = models.CharField(max_length=15, choices=ORG_TYPE)

    def __str__(self):
        return self.slug

    class Meta:
        db_table = 'organisation_organisation'
        verbose_name = _('Organisation')
        verbose_name_plural = _('Organisations')


class Speaker(TimeStampedModel):
    first_name = models.CharField(_('First Name'), max_length=120, blank=True)
    last_name = models.CharField(_('Last Name'), max_length=120, blank=True)
    email = models.EmailField(_('email address'), unique=True, db_index=True)
    about = models.TextField(max_length=10000)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'concourse_speaker'
        verbose_name = _('Speaker')
        verbose_name_plural = _('Speakers')


class Concourse(TimeStampedSlugModel):
    CONCOURSE_TYPE = (
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

    kind = models.CharField(max_length=15, choices=CONCOURSE_TYPE)
    event = models.ForeignKey("self", blank=True, null=True)
    speaker = models.ForeignKey(Speaker, null=True, blank=True, related_name='concourses')
    venue = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.slug

    class Meta:
        db_table = 'concourse_concourse'
        verbose_name = _('Concourse')
        verbose_name_plural = _('Concourses')


class SponsorCategory(models.Model):
    """To be added via Admin Panel(or Fixture), prior to adding Sponsors"""
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'concourse_sponsor_category'
        verbose_name = _('Sponsor Category')
        verbose_name_plural = _('Sponsor Categories')


class Sponsor(TimeStampedModel):
    concourse = models.ForeignKey(Concourse)
    organisation = models.ForeignKey(Organisation, null=True, blank=True)
    category = models.ForeignKey(SponsorCategory)

    class Meta:
        db_table = 'concourse_sponsor'
        verbose_name = _('Sponsor')
        verbose_name_plural = _('Sponsors')
