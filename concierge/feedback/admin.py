from django.contrib import admin

from . import models
from ..base.admin import HistoryExportAdmin


class FeedbackAdmin(HistoryExportAdmin):

    list_display = (
        'id',
        'created',
        'modified',
        'question',
        'text_response',
        'choice_response',
        'participant',
    )
    list_filter = ('created', 'modified', 'question', 'participant')


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Feedback, FeedbackAdmin)
