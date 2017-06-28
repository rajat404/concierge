from django.contrib import admin

from . import models
from ..base.admin import HistoryExportAdmin


class RegistrationAnswerAdmin(HistoryExportAdmin):

    list_display = (
        'id',
        'created',
        'modified',
        'question',
        'text_answer',
        'choice_answer',
        'is_attempted',
        'participant',
    )
    list_filter = (
        'created',
        'modified',
        'question',
        'is_attempted',
        'participant',
    )


class RegistrationQuizAdmin(HistoryExportAdmin):

    list_display = ('id', 'created', 'modified', 'quiz', 'participant')
    list_filter = ('created', 'modified', 'quiz', 'participant')
    raw_id_fields = ('answers',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.RegistrationAnswer, RegistrationAnswerAdmin)
_register(models.RegistrationQuiz, RegistrationQuizAdmin)
