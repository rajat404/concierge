from django.contrib import admin
from import_export.admin import ExportMixin
from simple_history.admin import SimpleHistoryAdmin


class ExportAdmin(ExportMixin, admin.ModelAdmin):
    """Adds export funcationality in the admin"""
    save_on_top = True


class HistoryExportAdmin(ExportAdmin, SimpleHistoryAdmin):
    """Adds export & history logging/viewing funcationality in the admin"""
    pass
