from django.contrib.postgres.fields import ArrayField, JSONField
from django.db import models
from django.utils.translation import ugettext_lazy as _
from simple_history.models import HistoricalRecords

from concierge.base.models import TimeStampedUUIDModel
from concierge.concourse.models import Concourse


class Question(TimeStampedUUIDModel):
    ANSWER_TYPES = (
        ('MCQ', 'MCQ'),
        ('PARAGRAPH', 'PARAGRAPH'),
        # ('FILE', 'FILE'),
        # ('DATETIME', 'DATETIME'),
        # ('OTHER', 'OTHER'),
    )

    CHOICE_TYPES = (
        ('TEXT', 'TEXT'),
        ('URL', 'URL'),
    )

    text = models.TextField(blank=False)
    kind = models.CharField(max_length=15, choices=ANSWER_TYPES)
    # description = models.CharField(max_length=50, blank=True)
    required = models.BooleanField(blank=False, help_text='is the question mandatory to attempt')
    editable = models.BooleanField(blank=False, help_text='can the answer be changed later')
    choices = JSONField(null=True)
    correct_choices = ArrayField(models.CharField(max_length=100, blank=True), null=True, blank=True,
                                 help_text='array field to support selection of multiple choices')
    history = HistoricalRecords(table_name='question_question_history')

    class Meta:
        db_table = 'quiz_question'
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')

    def __str__(self):
        return self.text


# class QuizType(models.Model):
#     """To be added via Admin Panel(or Fixture), prior to adding Quizzes"""
#     name = models.CharField(max_length=50, unique=True)

#     class Meta:
#         db_table = 'quiz_quiz_type'
#         verbose_name = _('Quiz Type')
#         verbose_name_plural = _('Quiz Types')

#     def __str__(self):
#         return self.name


class Quiz(TimeStampedUUIDModel):
    QUIZ_TYPES = (
        ('REGISTRATION', 'REGISTRATION'),
        ('FEEDBACK', 'FEEDBACK'),
    )
    label = models.CharField(max_length=100, unique=True)
    # kind = models.ForeignKey(QuizType, to_field='name')
    kind = models.CharField(max_length=50, choices=QUIZ_TYPES)
    concourse = models.ForeignKey(Concourse)
    questions = models.ManyToManyField(Question, blank=True, related_name='quizzes')

    class Meta:
        db_table = 'quiz_quiz'
        verbose_name = _('Quiz')
        verbose_name_plural = _('Quizzes')


class AnswerHelper(TimeStampedUUIDModel):
    question = models.ForeignKey(Question)
    text_answer = models.TextField(blank=True)
    choice_answer = ArrayField(models.CharField(max_length=100, blank=True), null=True, blank=True)
    is_attempted = models.BooleanField(default=False)

    class Meta:
        abstract = True
