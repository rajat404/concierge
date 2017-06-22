from django.contrib.postgres.fields import ArrayField, JSONField
from django.db import models
from django.utils.translation import ugettext_lazy as _

from concierge.base.models import UUIDModel, TimeStampedModel


class Questionnaire(TimeStampedModel, UUIDModel):
    RESPONSE_TYPES = (
        ('MCQ', 'MCQ'),
        ('PARAGRAPH', 'PARAGRAPH'),
        ('FILE', 'FILE'),
        # ('DATETIME', 'DATETIME'),
        # ('OTHER', 'OTHER'),
    )

    question = models.TextField(blank=False)
    # description = models.TextField(blank=True)
    kind = models.CharField(max_length=15, choices=RESPONSE_TYPES)
    label = models.CharField(max_length=50, blank=True)  # Short description for devs
    required = models.BooleanField(default=False, help_text='is the question mandatory to attempt')
    choices = JSONField(null=True)
    # Array field to support selection of multiple choices
    correct_choices = ArrayField(models.CharField(max_length=100, blank=True),
                                 null=True, blank=True)

    class Meta:
        db_table = 'questionnaire_questionnaire'
        verbose_name = _('Questionnaire')
        verbose_name_plural = _('Questionnaires')

    def __str__(self):
        return self.question


class QuestionnaireHelper(TimeStampedModel, UUIDModel):
    """Abstract model to use `Questionnaire` in your app

    After inheriting `QuestionnaireHelper` in your model,
    add a separate field for `User` or `Participant`, in order to maintain
    a relationship b/w the Questionnaire and those who attempted it
    """
    questionnaire = models.ForeignKey(Questionnaire)
    # User/Participant's response to the question
    text_response = models.TextField(blank=True)
    file_response = models.FileField(upload_to='file_response', blank=True)
    choice_response = ArrayField(models.CharField(max_length=100, blank=True),
                                 null=True, blank=True)

    class Meta:
        abstract = True
