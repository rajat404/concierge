from django.contrib import admin

from . import models
from ..base.admin import CommonAdmin


class FeedbackAdmin(CommonAdmin):

    list_display = (
        'id',
        'created',
        'modified',
        'questionnaire',
        'text_response',
        'file_response',
        'choice_response',
        'participant',
    )
    list_filter = ('created', 'modified', 'questionnaire', 'participant')


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Feedback, FeedbackAdmin)
