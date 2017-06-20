from django.contrib import admin

from . import models
from ..base.admin import CommonAdmin


class QuestionnaireAdmin(CommonAdmin):

    list_display = (
        'id',
        'created',
        'modified',
        'question',
        'kind',
        'required',
        'choices',
        'correct_choices',
    )
    list_filter = ('created', 'modified', 'required')


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Questionnaire, QuestionnaireAdmin)