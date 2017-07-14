# Third Party Stuff
from django import forms
from django.contrib import admin

# Concierge Stuff
from concierge.base.admin import ExportAdmin, HistoryExportAdmin

from . import models


class EventForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['start'] > cleaned_data['end']:
            raise forms.ValidationError('`end` must occur after `start`')
        if cleaned_data['participation_open']:
            error_msg = 'This field is required for `participation_open`'
            if not cleaned_data['participation_start']:
                self.add_error('participation_start', error_msg)
            if not cleaned_data['participation_end']:
                self.add_error('participation_end', error_msg)
        return cleaned_data


class OrganisationAdmin(HistoryExportAdmin):

    list_display = ('id', 'created', 'modified', 'name', 'slug', 'kind')
    list_filter = ('created', 'modified')
    search_fields = ('name', 'slug')


class SpeakerAdmin(HistoryExportAdmin):

    list_display = (
        'id',
        'created',
        'modified',
        'first_name',
        'last_name',
        'email',
        'about',
    )
    list_filter = ('created', 'modified')


class EventAdmin(HistoryExportAdmin):

    list_display = (
        'id',
        'created',
        'modified',
        'name',
        'slug',
        'registration_quiz',
        'feedback_quiz',
        'kind',
        'happening',
        'speaker',
        'venue',
        'description',
        'start',
        'end',
        'participation_open',
        'participation_start',
        'participation_end',
        'is_offline',
    )
    list_filter = (
        'created',
        'modified',
        'registration_quiz',
        'feedback_quiz',
        'happening',
        'speaker',
        'start',
        'end',
        'participation_open',
        'participation_start',
        'participation_end',
        'is_offline',
    )
    list_filter = ('created', 'modified')
    search_fields = ('name', 'slug')
    form = EventForm


class OfflineEventAdmin(HistoryExportAdmin):

    list_display = (
        'id',
        'created',
        'modified',
        'event',
        'longitude',
        'latitude',
        'address',
        'address_guidelines',
        'rsvp_open',
        'rsvp_start',
        'rsvp_end',
    )
    list_filter = (
        'created',
        'modified',
        'event',
        'rsvp_open',
        'rsvp_start',
        'rsvp_end',
    )
    list_filter = ('created', 'modified', 'event')


class SponsorCategoryAdmin(ExportAdmin):

    list_display = ('id', 'name')
    search_fields = ('name',)


class SponsorAdmin(HistoryExportAdmin):

    list_display = (
        'id',
        'created',
        'modified',
        'event',
        'organisation',
        'category',
    )
    list_filter = (
        'created',
        'modified',
        'event',
        'organisation',
        'category',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Organisation, OrganisationAdmin)
_register(models.Speaker, SpeakerAdmin)
_register(models.Event, EventAdmin)
_register(models.OfflineEvent, OfflineEventAdmin)
_register(models.SponsorCategory, SponsorCategoryAdmin)
_register(models.Sponsor, SponsorAdmin)
