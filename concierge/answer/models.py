# Third Party Stuff
from django.db import models
from django.utils.translation import ugettext_lazy as _
from simple_history.models import HistoricalRecords

# Concierge Stuff
from concierge.participant.models import Participant
from concierge.quiz.models import AnswerHelper


class Answer(AnswerHelper):
    """AnswerHelper adds the fields - id(UUID), question, text_answer,
    choice_answer, created, modified
    """
    history = HistoricalRecords(table_name='answer_history')
    participant = models.ForeignKey(Participant, related_name='answers')

    class Meta:
        unique_together = ('question', 'participant')
        db_table = 'quiz_answer'
        verbose_name = _('Answer')
        verbose_name_plural = _('Answers')

    def __str__(self):
        return str(self.id)
