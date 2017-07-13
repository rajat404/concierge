# Third Party Stuff
from django.contrib import admin

# Concierge Stuff
from concierge.base.admin import HistoryExportAdmin

from . import models


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


_register(models.Answer, AnswerAdmin)
