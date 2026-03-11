from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Book
# Register your models here.

@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    pass