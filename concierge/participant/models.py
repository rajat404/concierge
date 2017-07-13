# Third Party Stuff
from django.db import models
from django.utils.translation import ugettext_lazy as _
from simple_history.models import HistoricalRecords

# Concierge Stuff
from concierge.base.models import TimeStampedUUIDModel
from concierge.event.models import Event
from concierge.users.models import User


class TshirtSize(models.Model):
    """To be added via Admin Panel(or Fixture), prior to adding Participants"""
    size = models.CharField(max_length=30, unique=True)

    class Meta:
        db_table = 'participant_tshirt_size'
        verbose_name = _('Tshirt Size')
        verbose_name_plural = _('Tshirt Sizes')

    def __str__(self):
        return self.size


class ParticipantType(models.Model):
    """To be added via Admin Panel(or Fixture), prior to adding Participants"""
    kind = models.CharField(max_length=30, unique=True)

    class Meta:
        db_table = 'participant_type'
        verbose_name = _('Participant Type')
        verbose_name_plural = _('Participant Types')

    def __str__(self):
        return self.kind


class Participant(TimeStampedUUIDModel):
    user = models.ForeignKey(User)
    event = models.ForeignKey(Event)
    kind = models.ForeignKey(ParticipantType, to_field='kind', null=True, blank=True)
    tshirt_size = models.ForeignKey(TshirtSize, to_field='size', null=True, blank=True)
    history = HistoricalRecords(table_name='participant_participant_history')

    class Meta:
        db_table = 'participant_participant'
        verbose_name = _('Participant')
        verbose_name_plural = _('Participants')

    def __str__(self):
        return str(self.id)
