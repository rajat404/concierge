from django.db import models
from django.utils.translation import ugettext_lazy as _
from simple_history.models import HistoricalRecords

from concierge.participant.models import Participant
from concierge.quiz.models import AnswerHelper


class Answer(AnswerHelper):
    """`AnswerHelper adds the fields - question, text_answer, choice_answer"""
    participant = models.ForeignKey(Participant, related_name='answers')
    history = HistoricalRecords(table_name='answer_history')

    class Meta:
        unique_together = ('question', 'participant')
        db_table = 'quiz_answer'
        verbose_name = _('Answer')
        verbose_name_plural = _('Answers')



# class QuizAnswer(TimeStampedUUIDModel):
#     """Log of all answers for a quiz by a participant"""
#     quiz = models.ForeignKey(Quiz)
#     answers = models.ManyToManyField(Answer, related_name='quiz_answers')
#     participant = models.ForeignKey(Participant, related_name='quiz_answers')
#     history = HistoricalRecords(table_name='quiz_answer_history')

#     class Meta:
#         db_table = 'quiz_quiz_answer'
#         verbose_name = _('Quiz Answer')
#         verbose_name_plural = _('Quiz Answers')
