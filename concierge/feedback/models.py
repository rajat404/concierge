from concierge.base.models import TimeStampedModel
from concierge.questionnaire.models import Questionnaire
from concierge.registration.models import Participant
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Feedback(TimeStampedModel):
    participant = models.ForeignKey(Participant, related_name='feedbacks')
    questionnaire = models.ForeignKey(Questionnaire)
    # Participant's response to the question
    text_response = models.TextField()
    choice_response = ArrayField(models.CharField(max_length=100, blank=True),
                                 null=True, blank=True)

    class Meta:
        db_table = 'feedback_feedback'
        verbose_name = _('Feedback')
        verbose_name_plural = _('Feedback')
