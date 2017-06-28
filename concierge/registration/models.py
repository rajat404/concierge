from django.db import models
from django.utils.translation import ugettext_lazy as _
from simple_history.models import HistoricalRecords

from concierge.base.models import TimeStampedUUIDModel
from concierge.participant.models import Participant
from concierge.quiz.models import AnswerHelper, Quiz


class RegistrationAnswer(AnswerHelper):
    """Holds each participant's answer to each question"""

    # TODO: remove before release
    # Fields of the Abstract model are mentioned below,
    # solely for better visibility during development

    # question = models.ForeignKey(Question)
    # text_answer = models.TextField(blank=True)
    # choice_answer = ArrayField(models.CharField(max_length=100, blank=True), null=True, blank=True)
    # is_attempted = models.BooleanField(default=False)

    participant = models.ForeignKey(Participant, related_name='registration_answers')
    history = HistoricalRecords(table_name='registration_answer_history')

    class Meta:
        db_table = 'registration_answer'
        verbose_name = _('Registration Answer')
        verbose_name_plural = _('Registration Answers')


class RegistrationQuiz(TimeStampedUUIDModel):
    """Log of all answers for a quiz by a participant"""
    quiz = models.ForeignKey(Quiz)
    answers = models.ManyToManyField(RegistrationAnswer, related_name='registration_quiz_answers')
    participant = models.ForeignKey(Participant, related_name='registration_quiz_answers')
    history = HistoricalRecords(table_name='registration_quiz_answer_history')

    class Meta:
        db_table = 'registration_quiz_answer'
        verbose_name = _('Registration Quiz Answer')
        verbose_name_plural = _('Registration Quiz Answers')
