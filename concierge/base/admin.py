from django.contrib import admin
from import_export.admin import ExportMixin


class CommonAdmin(ExportMixin, admin.ModelAdmin):
    save_on_top = True
