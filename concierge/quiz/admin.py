from django.contrib import admin

from . import models
from ..base.admin import HistoryExportAdmin


class QuestionAdmin(HistoryExportAdmin):

    list_display = (
        'id',
        'created',
        'modified',
        'text',
        'kind',
        'required',
        'editable',
        'choices',
        'correct_choices',
    )
    list_filter = ('created', 'modified', 'required', 'editable')


class QuizAdmin(HistoryExportAdmin):

    list_display = (
        'id',
        'created',
        'modified',
        'label',
        'kind',
        'concourse',
    )
    list_filter = ('created', 'modified', 'concourse')
    raw_id_fields = ('questions',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Question, QuestionAdmin)
_register(models.Quiz, QuizAdmin)
