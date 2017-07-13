# Third Party Stuff
from django.contrib import admin

# Concierge Stuff
from concierge.base.admin import ExportAdmin, HistoryExportAdmin

from . import models


class TshirtSizeAdmin(ExportAdmin):

    list_display = ('id', 'size')


class ParticipantTypeAdmin(ExportAdmin):

    list_display = ('id', 'kind')


class ParticipantAdmin(HistoryExportAdmin):

    list_display = (
        'id',
        'created',
        'modified',
        'user',
        'event',
        'kind',
        'tshirt_size',
    )
    list_filter = (
        'created',
        'modified',
        'user',
        'event',
        'kind',
        'tshirt_size',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.TshirtSize, TshirtSizeAdmin)
_register(models.ParticipantType, ParticipantTypeAdmin)
_register(models.Participant, ParticipantAdmin)
