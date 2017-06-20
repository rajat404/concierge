from concierge.base.models import TimeStampedModel
from concierge.concourse.models import Concourse
from concierge.users.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class TshirtSize(models.Model):
    """To be added via Admin Panel(or Fixture), prior to adding Participants"""
    size = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.size

    class Meta:
        db_table = 'participant_tshirt_size'
        verbose_name = _('Tshirt Size')
        verbose_name_plural = _('Tshirt Sizes')


class ParticipantType(models.Model):
    """To be added via Admin Panel(or Fixture), prior to adding Participants"""
    kind = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.kind

    class Meta:
        db_table = 'participant_type'
        verbose_name = _('Participant Type')
        verbose_name_plural = _('Participant Types')


class Participant(TimeStampedModel):
    user = models.ForeignKey(User)
    concourse = models.ForeignKey(Concourse)
    kind = models.ForeignKey(ParticipantType, to_field='kind', null=True, blank=True)
    tshirt_size = models.ForeignKey(TshirtSize, to_field='size', null=True, blank=True)

    class Meta:
        db_table = 'participant_participant'
        verbose_name = _('Participant')
        verbose_name_plural = _('Participants')
