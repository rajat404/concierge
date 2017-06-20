from concierge.base.models import TimeStampedModel
from concierge.participant.models import Participant
from concierge.questionnaire.models import Questionnaire
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Registration(TimeStampedModel):
    participant = models.ForeignKey(Participant, related_name='registrations')
    questionnaire = models.ForeignKey(Questionnaire)
    text_response = models.TextField(blank=True)
    # Participant's response to the question
    file_response = models.FileField(upload_to='file_response', blank=True)
    choice_response = ArrayField(models.CharField(max_length=100, blank=True),
                                 null=True, blank=True)

    class Meta:
        db_table = 'registration_registration'
        verbose_name = _('Registration')
        verbose_name_plural = _('Registrations')
