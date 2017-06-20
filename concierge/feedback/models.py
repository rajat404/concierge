from concierge.questionnaire.models import QuestionnaireHelper
from concierge.registration.models import Participant
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Feedback(QuestionnaireHelper):
    participant = models.ForeignKey(Participant, related_name='feedbacks')

    class Meta:
        db_table = 'feedback_feedback'
        verbose_name = _('Feedback')
        verbose_name_plural = _('Feedback')
