from django.contrib import admin

from concierge.base.admin import HistoryExportAdmin

from . import models


class HistoricalAnswerAdmin(HistoryExportAdmin):

    list_display = (
        'id',
        'created',
        'modified',
        'text_answer',
        'choice_answer',
        'question',
        'participant',
        'history_id',
        'history_date',
        'history_change_reason',
        'history_user',
        'history_type',
    )
    list_filter = (
        'created',
        'modified',
        'question',
        'participant',
        'history_date',
        'history_user',
    )


class AnswerAdmin(HistoryExportAdmin):

    list_display = (
        'id',
        'created',
        'modified',
        'question',
        'text_answer',
        'choice_answer',
        'participant',
    )
    list_filter = ('created', 'modified', 'question', 'participant')


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.HistoricalAnswer, HistoricalAnswerAdmin)
_register(models.Answer, AnswerAdmin)
