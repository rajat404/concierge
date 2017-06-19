from django.contrib import admin

from . import models


class TshirtSizeAdmin(admin.ModelAdmin):

    list_display = ('id', 'size')


class ParticipantTypeAdmin(admin.ModelAdmin):

    list_display = ('id', 'kind')


class ParticipantAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'created',
        'modified',
        'user',
        'concourse',
        'kind',
        'tshirt_size',
    )
    list_filter = (
        'created',
        'modified',
        'user',
        'concourse',
        'kind',
        'tshirt_size',
    )


class RegistrationAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'created',
        'modified',
        'participant',
        'questionnaire',
        'response',
    )
    list_filter = ('created', 'modified', 'participant', 'questionnaire')


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.TshirtSize, TshirtSizeAdmin)
_register(models.ParticipantType, ParticipantTypeAdmin)
_register(models.Participant, ParticipantAdmin)
_register(models.Registration, RegistrationAdmin)
