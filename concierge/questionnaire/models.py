from concierge.base.models import TimeStampedModel
from django.contrib.postgres.fields import ArrayField, JSONField
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Questionnaire(TimeStampedModel):
    QUESTIONNAIRE_TYPES = (
        ('MCQ', 'MCQ'),
        ('PARAGRAPH', 'PARAGRAPH'),
        # ('DATETIME', 'DATETIME'),
        # ('OTHER', 'OTHER'),
    )

    question = models.TextField(blank=False)
    description = models.TextField(blank=True)
    kind = models.CharField(max_length=15, choices=QUESTIONNAIRE_TYPES)
    required = models.BooleanField(default=False)
    paragraph = models.TextField(blank=True)
    choices = JSONField(null=True)
    correct_choices = ArrayField(models.CharField(max_length=100, blank=True),
                                null=True, blank=True)

    def __str__(self):
        return self.slug

    class Meta:
        db_table = 'questionnaire_questionnaire'
        verbose_name = _('Questionnaire')
        verbose_name_plural = _('Questionnaires')
