# Third Party Imports
from django.contrib.postgres.fields import ArrayField, JSONField
from django.db import models
from django.utils.translation import ugettext_lazy as _
from simple_history.models import HistoricalRecords

# Concierge Imports
from concierge.base.models import TimeStampedModel, UUIDModel


class Question(UUIDModel, TimeStampedModel):
    ANSWER_CHOICES = (
        ('MCQ', 'MCQ'),
        ('PARAGRAPH', 'PARAGRAPH'),
        # ('FILE', 'FILE'),
        # ('DATETIME', 'DATETIME'),
        # ('OTHER', 'OTHER'),
    )

    CHOICE_TYPES = (
        ('TEXT', 'TEXT'),
        ('URL', 'URL'),
        ('OTHER', 'OTHER'),
    )

    history = HistoricalRecords(table_name='question_question_history')
    text = models.TextField(blank=False, unique=True)
    kind = models.CharField(max_length=15, choices=ANSWER_CHOICES)
    # description = models.CharField(max_length=50, blank=True)
    required = models.BooleanField(blank=False, help_text='is the question mandatory to attempt')
    editable = models.BooleanField(blank=False, help_text='can the answer be changed later')
    choices = JSONField(null=True)
    correct_choices = ArrayField(models.CharField(max_length=100, blank=True), null=True, blank=True,
                                 help_text='array field to support selection of multiple choices')

    class Meta:
        db_table = 'quiz_question'
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')

    def __str__(self):
        return str(self.id)


class Quiz(UUIDModel, TimeStampedModel):
    label = models.CharField(max_length=100, unique=True)
    questions = models.ManyToManyField(Question, blank=True, related_name='quizzes')

    class Meta:
        db_table = 'quiz_quiz'
        verbose_name = _('Quiz')
        verbose_name_plural = _('Quizzes')

    def __str__(self):
        return self.label


class AnswerHelper(UUIDModel, TimeStampedModel):
    question = models.ForeignKey(Question, related_name='answers')
    text_answer = models.TextField(blank=True)
    choice_answer = ArrayField(models.CharField(max_length=100, blank=True), null=True, blank=True)

    class Meta:
        abstract = True
