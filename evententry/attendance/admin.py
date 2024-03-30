from django.contrib import admin
from import_export.admin import ImportExportMixin

from .models import Student, ActiveDay


class BaseImportExportAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

@admin.register(Student)
class StudentAdmin(BaseImportExportAdmin):
    pass

admin.site.register(ActiveDay)