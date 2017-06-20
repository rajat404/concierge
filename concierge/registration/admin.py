from django.contrib import admin

from . import models
from ..base.admin import CommonAdmin


class RegistrationAdmin(CommonAdmin):

    list_display = (
        'id',
        'created',
        'modified',
        'participant',
        'questionnaire',
        'text_response',
        'file_response',
        'choice_response',
    )
    list_filter = ('created', 'modified', 'participant', 'questionnaire')


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Registration, RegistrationAdmin)
