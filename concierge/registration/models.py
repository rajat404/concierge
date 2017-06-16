from concierge.base.models import TimeStampedModel
from concierge.concourse.models import Concourse
from concierge.questionnaire.models import Questionnaire
from concierge.users.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class TshirtSize(models.Model):
    size = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'participant_tshirt_size'
        verbose_name = _('TshirtSize')
        verbose_name_plural = _('TshirtSizes')


class ParticipantType(models.Model):
    kind = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'participant_type'
        verbose_name = _('ParticipantType')
        verbose_name_plural = _('ParticipantTypes')


class Participant(TimeStampedModel):
    user = models.ForeignKey(User)
    concourse = models.ForeignKey(Concourse)
    kind = models.ForeignKey(ParticipantType, to_field='kind', null=True, blank=True)
    tshirt_size = models.ForeignKey(TshirtSize, to_field='size', null=True, blank=True)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'participant_participant'
        verbose_name = _('Participant')
        verbose_name_plural = _('Participants')


class Registration(TimeStampedModel):
    participant = models.ForeignKey(Participant, related_name='registration')
    questionnaire = models.ForeignKey(Questionnaire)
    response = models.TextField()  # Participant's response to the question

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'registration_registration'
        verbose_name = _('Registration')
        verbose_name_plural = _('Registrations')
