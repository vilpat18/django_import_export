from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin
from .models import Book,Author

@admin.register(Book,Author)
class BookResource(ImportExportModelAdmin):
    pass