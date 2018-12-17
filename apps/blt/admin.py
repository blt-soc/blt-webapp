from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
from .resources import *

@admin.register(Address)

@admin.register(Transaction)
class TransactionAdmin(ImportExportModelAdmin):
    resource_class = TransactionResource
