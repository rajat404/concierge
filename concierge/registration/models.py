from concierge.participant.models import Participant
from concierge.questionnaire.models import QuestionnaireHelper
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Registration(QuestionnaireHelper):
    participant = models.ForeignKey(Participant, related_name='registrations')

    class Meta:
        db_table = 'registration_registration'
        verbose_name = _('Registration')
        verbose_name_plural = _('Registrations')
