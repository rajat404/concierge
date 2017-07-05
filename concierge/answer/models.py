from django.db import models
from django.utils.translation import ugettext_lazy as _
from simple_history.models import HistoricalRecords

from concierge.participant.models import Participant
from concierge.quiz.models import AnswerHelper


class Answer(AnswerHelper):
    """`AnswerHelper adds the fields - id(UUID), question, text_answer,
    choice_answer, created, modified
    """
    participant = models.ForeignKey(Participant, related_name='answers')
    history = HistoricalRecords(table_name='answer_history')

    class Meta:
        unique_together = ('question', 'participant')
        db_table = 'quiz_answer'
        verbose_name = _('Answer')
        verbose_name_plural = _('Answers')
