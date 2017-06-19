from django.contrib import admin

from . import models


class OrganisationAdmin(admin.ModelAdmin):

    list_display = ('id', 'created', 'modified', 'name', 'slug', 'kind')
    list_filter = ('created', 'modified')
    search_fields = ('name', 'slug')


class SpeakerAdmin(admin.ModelAdmin):

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


class ConcourseAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'created',
        'modified',
        'name',
        'slug',
        'kind',
        'event',
        'speaker',
    )
    list_filter = ('created', 'modified', 'event', 'speaker')
    search_fields = ('name', 'slug')


class SponsorCategoryAdmin(admin.ModelAdmin):

    list_display = ('id', 'name')
    search_fields = ('name',)


class SponsorAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'created',
        'modified',
        'concourse',
        'organisation',
        'category',
    )
    list_filter = (
        'created',
        'modified',
        'concourse',
        'organisation',
        'category',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Organisation, OrganisationAdmin)
_register(models.Speaker, SpeakerAdmin)
_register(models.Concourse, ConcourseAdmin)
_register(models.SponsorCategory, SponsorCategoryAdmin)
_register(models.Sponsor, SponsorAdmin)
