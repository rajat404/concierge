from django.db import models
from django.utils.translation import ugettext_lazy as _
from simple_history.models import HistoricalRecords

from concierge.quiz.models import ResponseHelper
from concierge.registration.models import Participant


class Feedback(ResponseHelper):
    participant = models.ForeignKey(Participant, related_name='feedbacks')
    history = HistoricalRecords(table_name='feedback_feedback_history')

    class Meta:
        db_table = 'feedback_feedback'
        verbose_name = _('Feedback')
        verbose_name_plural = _('Feedback')
