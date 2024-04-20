from django.contrib import admin
from import_export.admin import ImportExportMixin

from .models import Student, ActiveDay


class BaseImportExportAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

@admin.register(Student)
class StudentAdmin(BaseImportExportAdmin):
    list_display = ('name', 'college_email',  'is_hosteler','student_number', 'branch', 'gender', 'is_present_day1', 'is_present_day2', 'is_present_day3', 'is_present_day4')
    search_fields = ['name', 'student_number']
    list_filter = ['gender', 'is_present_day1', 'is_present_day2', 'is_present_day3', 'is_present_day4']

admin.site.register(ActiveDay)